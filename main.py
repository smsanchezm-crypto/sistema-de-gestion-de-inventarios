from servicios.inventario import Inventario

def menu():
    inventario = Inventario()

    # Menú interactivo en consola
    while True:
        print("\n=== Sistema de Gestión de Inventarios ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            resultado = inventario.agregar_producto(id, nombre, cantidad, precio)
            if resultado is None:
                print(f"Error: ya existe un producto con el ID '{id}'.")
            elif resultado:
                print("Producto agregado y guardado en el archivo correctamente.")
            else:
                print("Producto agregado en memoria pero no se pudo guardar en el archivo.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            resultado = inventario.eliminar_producto(id)
            if resultado is None:
                print(f"No se encontró un producto con el ID '{id}'.")
            elif resultado:
                print("Producto eliminado y archivo actualizado correctamente.")
            else:
                print("Producto eliminado de memoria pero no se pudo actualizar el archivo.")

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            print("Deje en blanco si no desea cambiar el campo.")
            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            resultado = inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)
            if resultado is None:
                print(f"No se encontró un producto con el ID '{id}'.")
            elif resultado:
                print("Producto actualizado y archivo sincronizado correctamente.")
            else:
                print("Producto actualizado en memoria pero no se pudo sincronizar el archivo.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            if not inventario.buscar_por_nombre(nombre):
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            if not inventario.listar_productos():
                print("El inventario está vacío.")

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
    