while True:
    print("\n--- Menú Principal ---")
    print("1. Opciones del inventario")
    print("2. Opciones de las Facturas")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        while True:
            print("\nElija la acción que desea realizar: ")
            print("1 Agregar artículo al inventario")
            print("2 Borrar artículo del inventario")
            print("3 Editar artículo del inventario")
            print("4 Ver artículos guardados")
            print("5 Buscar producto por id o nombre")
            print("6 Salir")

            x = input("Elija la acción que desea realizar: ")

            if x == "1":   
                articulo = input("Escriba el nombre del artículo que desea agregar: ")
                precio = int(input("Escriba el precio del artículo: "))
                cantidad = int(input("Escriba la cantidad del artículo: "))     
                with open("inventario.txt", "a") as archivo:
                    archivo.write(f"{articulo},  {precio},  {cantidad}  \n")
                print("Se agrego el artículo")
            elif x == "2":
                try:
                    with open("inventario.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay artículos para borrar")
                    continue

                if len(lineas) == 0:
                    print("No hay artículos para borrar")
                    continue

                for numero, linea in enumerate(lineas, 1):    
                    print(f"{numero}. {linea.strip()}")

                try:
                    numero_articulo = int(input("Ingrese el número del artículo a borrar: "))
                    if numero_articulo < 1 or numero_articulo > len(lineas):
                        print("Número de registro inválido")
                        continue
                except ValueError:
                    print("Entrada inválida, debe ser un número")
                    continue

                articulo_borrar = lineas[numero_articulo - 1].strip()
                print(f"Vas a borrar el artículo: {articulo_borrar}")

                confirmar = input("¿Está seguro de borrar el registro? (si/no): ")
                if confirmar.lower() == 'si':
                    del lineas[numero_articulo - 1]
                    with open("inventario.txt", "w") as archivo:
                        archivo.writelines(lineas)
                    print("Se borró el registro.")
                else:
                    print("Operación cancelada.")

            elif x == "3":
                try:
                    with open("inventario.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay artículos para editar")
                    continue

                if len(lineas) == 0:
                    print("No hay artículos para editar")
                    continue

                for numero, linea in enumerate(lineas, 1):
                    print(f"{numero}. {linea.strip()}")

                try:
                    numero_articulo = int(input("Ingrese el número del artículo que desea editar: "))
                    if numero_articulo < 1 or numero_articulo > len(lineas):
                        print("Número de artículo inválido")
                        continue
                except ValueError:
                    print("Entrada inválida, debe ser un número")
                    continue

                articulo_actual = lineas[numero_articulo - 1].strip()
                print(f"Editando artículo: {articulo_actual}")

                nuevo_nombre = input("Ingrese el nuevo nombre del artículo: ")
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

                lineas[numero_articulo - 1] = f"{nuevo_nombre}  ,  {nuevo_precio}  ,  {nueva_cantidad}\n"

                with open("inventario.txt", "w") as archivo:
                    archivo.writelines(lineas)
                print("Artículo editado.")
            elif x == "4":
                try:
                    with open("inventario.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay productos en el inventario todavía")
                    continue

                if len(lineas) == 0:
                    print("No hay productos en el inventario todavía")
                else:
                    print("\n--- Inventario completo ---")
                    for numero, linea in enumerate(lineas, 1):
                        datos = linea.strip().split(",")
                        if len(datos) == 3:
                            nombre, precio, cantidad = datos
                            print(f"{numero}. Nombre: {nombre}, Precio: {precio}, Stock: {cantidad}")
                        else:
                            print(f"{numero}. Registro inválido -> {linea.strip()}")
            elif x == "5":
                try:
                    with open("inventario.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay productos en el inventario todavía")
                    continue

                if len(lineas) == 0:
                    print("No hay productos en el inventario todavía")
                    continue

                busqueda = input("Ingrese el ID (número) o el nombre del producto: ")

                encontrado = False
                if busqueda.isdigit():
                    numero = int(busqueda)
                    if 1 <= numero <= len(lineas):
                        nombre, precio, cantidad = lineas[numero-1].strip().split(",")
                        print(f"Encontrado -> ID {numero}: Nombre: {nombre} | Precio: {precio}  Stock: {cantidad}")
                        encontrado = True
                    else:
                        print("No existe un producto con ese ID")
                else:
                    for numero, linea in enumerate(lineas, 1):
                        nombre, precio, cantidad = linea.strip().split(",")
                        if busqueda.lower() == nombre.strip().lower():
                            print(f"Encontrado -> ID {numero}: Nombre: {nombre.strip()} | Precio: {precio.strip()} | Stock: {cantidad.strip()}")
                            encontrado = True
                            break

                    if not encontrado:
                        print("No existe un producto con ese nombre")
                        
            elif x == "6":
                print("Saliendo del programa...")
                break

            else:
                print("Por favor, ingrese una opción válida")
                pass
    elif opcion == "2":
        while True:
            print("\n--- Menú Facturas ---")
            print("1. Crear factura")
            print("2. Listar facturas")
            print("3. Ver detalle de factura")
            print("4. Editar factura")
            print("5. Eliminar factura")
            print("6. Volver al menú principal")

            f = input("Elija una acción: ")

            if f == "1":
                print("\n--- Crear nueva factura ---")
                try:
                    with open("facturas.txt", "r") as archivo:
                        lineas = archivo.readlines()
                        ultimo_id = int(lineas[-1].split(",")[0]) if lineas else 0
                except FileNotFoundError:
                    ultimo_id = 0

                id_factura = ultimo_id + 1
                cliente = input("Ingrese el nombre del cliente: ")

                items = []
                while True:
                    producto = input("Nombre del producto o 'fin' para terminar la factura: ")
                    if producto.lower() == "fin":
                        break
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio unitario: "))
                    items.append((producto, cantidad, precio))

                subtotal = sum(c * p for _, c, p in items)
                iva = subtotal * 0.19
                total = subtotal + iva
                def limpiar_numero(n):
                    return int(n) if n.is_integer() else round(n, 2)

                subtotal_str = limpiar_numero(subtotal)
                iva_str = limpiar_numero(iva)
                total_str = limpiar_numero(total)

                items_limpios = []
                for producto, cantidad, precio in items:
                    precio_limpio = limpiar_numero(precio)
                    items_limpios.append((producto, cantidad, precio_limpio))

                with open("facturas.txt", "a") as archivo:
                    archivo.write(f"{id_factura},{cliente},S:{subtotal_str},I:{iva_str},T:{total_str},{items_limpios}\n")

                print("\nFactura creada con éxito ")
                print(f"ID: {id_factura} | Cliente: {cliente}")
                print(f"Subtotal: {subtotal_str}, IVA: {iva_str}, Total: {total_str}")
                pass
            elif f == "2":
                try:
                    with open("facturas.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay facturas registradas")
                    continue

                if not lineas:
                    print("No hay facturas registradas")
                else:
                    print("\n--- Lista de Facturas ---")
                    for linea in lineas:
                        partes = linea.strip().split(",")
                        if len(partes) >= 5:
                            id_factura, cliente, subtotal, iva, total, *_ = partes
                            print(f"ID: {id_factura} , Cliente: {cliente},{subtotal}, {iva}, {total}")
                pass
            elif f == "3":
                id_buscar = input("Ingrese el ID de la factura: ")
                try:
                    with open("facturas.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay facturas registradas")
                    continue

                encontrado = False
                for linea in lineas:
                    partes = linea.strip().split(",", 5) 
                    if partes[0] == id_buscar:
                        print("\n--- Detalle de factura ---")
                        print(f"ID: {partes[0]} | Cliente: {partes[1]}")
                        print(f"{partes[2]}, {partes[3]}, {partes[4]}")
                        print(f"Items: {partes[5]}")
                        encontrado = True
                        break
                if not encontrado:
                    print("No existe factura con ese ID.")
                pass
            elif f == "4":
                try:
                    with open("facturas.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay facturas registradas")
                    continue

                if not lineas:
                    print("No hay facturas registradas")
                    continue
                print("\n--- Facturas disponibles ---")
                for linea in lineas:
                    partes = linea.strip().split(",")
                    if len(partes) >= 5:
                        id_factura, cliente, subtotal, iva, total, *_ = partes
                        print(f"ID: {id_factura} | Cliente: {cliente} | {subtotal} | {iva} | {total}")

                id_editar = input("Ingrese el ID de la factura que desea editar: ")
                indice = None

                for i, linea in enumerate(lineas):
                    if linea.startswith(id_editar + ","):
                        indice = i
                        break

                if indice is None:
                    print(" No existe factura con ese ID.")
                    continue
                print("\n--- Editando Factura ---")
                nuevo_cliente = input("Ingrese el nuevo nombre del cliente: ")
                items = []
                while True:
                    producto = input("Nombre del producto o 'fin' para terminar: ")
                    if producto.lower() == "fin":
                        break
                    try:
                        cantidad = int(input("Cantidad: "))
                        precio = float(input("Precio unitario: "))
                    except ValueError:
                        print("Entrada inválida, intente de nuevo.")
                        continue
                    items.append((producto, cantidad, precio))

                if not items:
                    print("No se registraron productos. Operación cancelada.")
                    continue
                subtotal = sum(c * p for _, c, p in items)
                iva = subtotal * 0.19
                total = subtotal + iva

                def limpiar_numero(n):
                    return int(n) if n.is_integer() else round(n, 2)

                subtotal_str = limpiar_numero(subtotal)
                iva_str = limpiar_numero(iva)
                total_str = limpiar_numero(total)

                items_limpios = []
                for producto, cantidad, precio in items:
                    precio_limpio = limpiar_numero(precio)
                    items_limpios.append((producto, cantidad, precio_limpio))
                lineas[indice] = f"{id_editar},{nuevo_cliente},S:{subtotal_str},I:{iva_str},T:{total_str},{items_limpios}\n"

                with open("facturas.txt", "w") as archivo:
                    archivo.writelines(lineas)

                print("Factura editada con éxito.")
                pass
            elif f == "5":
                id_borrar = input("Ingrese el ID de la factura a eliminar: ")
                try:
                    with open("facturas.txt", "r") as archivo:
                        lineas = archivo.readlines()
                except FileNotFoundError:
                    print("No hay facturas registradas")
                    continue

                nuevas = []
                eliminado = False
                for linea in lineas:
                    if linea.startswith(id_borrar + ","):
                        eliminado = True
                    else:
                        nuevas.append(linea)

                if eliminado:
                    with open("facturas.txt", "w") as archivo:
                        archivo.writelines(nuevas)
                    print("Factura eliminada con éxito.")
                else:
                    print("No existe factura con ese ID.")

                pass
            elif f == "6":
                break
            else:
                print("Opción inválida")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")