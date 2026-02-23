from modelos.producto import Producto

# Clase que gestiona las operaciones del inventario
# Usa una lista como estructura principal de almacenamiento.
class Inventario:
    def __init__(self):
        # Lista principal donde se almacenan los productos
        self.__productos = []

    def agregar_producto(self, id, nombre, cantidad, precio):
        # Validar que no exista otro producto con el mismo ID
        for p in self.__productos:
            if p.get_id() == id:
                print(f"Ya existe un producto con el ID {id}.")
                return
        nuevo = Producto(id, nombre, cantidad, precio)
        self.__productos.append(nuevo)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        # Buscar el producto por ID y eliminarlo de la lista
        for p in self.__productos:
            if p.get_id() == id:
                self.__productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        # Actualizar cantidad y/o precio según los valores proporcionados
        for p in self.__productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado correctamente.")
                return
        print("No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        # Retorna la lista de productos cuyo nombre contenga el texto ingresado
        # (coincidencia parcial, sin distinguir mayúsculas)
        resultados = [p for p in self.__productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                self.__mostrar_producto(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def listar_productos(self):
        # Mostrar todos los productos registrados en el inventario
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario ---")
            for p in self.__productos:
                self.__mostrar_producto(p)

    def __mostrar_producto(self, p):
        print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")
        