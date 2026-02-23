from modelos.producto import Producto

# Nombre del archivo donde se persiste el inventario
ARCHIVO_INVENTARIO = "inventario.txt"

# Clase que gestiona las operaciones del inventario.
# Usa una lista como estructura principal de almacenamiento
# y un archivo de texto para persistir los datos.
class Inventario:
    def __init__(self):
        # Lista principal donde se almacenan los productos
        self.__productos = []
        # Al iniciar, cargar los productos guardados en el archivo
        self.__cargar_desde_archivo()

    # --- Operaciones del inventario ---

    def agregar_producto(self, id, nombre, cantidad, precio):
        # Validar que no exista otro producto con el mismo ID
        for p in self.__productos:
            if p.get_id() == id:
                return None
        nuevo = Producto(id, nombre, cantidad, precio)
        self.__productos.append(nuevo)
        return self.__guardar_en_archivo()
        

    def eliminar_producto(self, id):
        # Buscar el producto por ID y eliminarlo de la lista
        for p in self.__productos:
            if p.get_id() == id:
                self.__productos.remove(p)
                return self.__guardar_en_archivo()
        return None

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        # Actualizar cantidad y/o precio según los valores proporcionados
        for p in self.__productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return self.__guardar_en_archivo()
        return None

    def buscar_por_nombre(self, nombre):
        # Retorna la lista de productos cuyo nombre contenga el texto ingresado
        # (coincidencia parcial, sin distinguir mayúsculas)
        resultados = [p for p in self.__productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print(f"\n--- Resultados para '{nombre}' ---")
            for p in resultados:
                self.__mostrar_producto(p)
            return True
        return False

    def listar_productos(self):
        # Mostrar todos los productos registrados en el inventario
        if self.__productos:
            print("\n--- Inventario ---")
            for p in self.__productos:
                self.__mostrar_producto(p)
            return True
        return False

    # --- Manejo de archivos ---

    def __guardar_en_archivo(self):
        # Escribir todos los productos en el archivo, uno por línea.
        # Formato de cada línea: id,nombre,cantidad,precio
        try:
            with open(ARCHIVO_INVENTARIO, "w") as archivo:
                for p in self.__productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    archivo.write(linea)
            return True
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")
            return False

    def __cargar_desde_archivo(self):
        # Leer el archivo y reconstruir la lista de productos al iniciar el programa
        try:
            with open(ARCHIVO_INVENTARIO, "r") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    # Ignorar líneas vacías o con formato incorrecto
                    if not linea:
                        continue
                    partes = linea.split(",")
                    if len(partes) != 4:
                        print(f"Advertencia: línea con formato incorrecto ignorada -> '{linea}'")
                        continue
                    try:
                        id = partes[0]
                        nombre = partes[1]
                        cantidad = int(partes[2])
                        precio = float(partes[3])
                        self.__productos.append(Producto(id, nombre, cantidad, precio))
                    except ValueError:
                        # Si cantidad o precio no son números válidos, se ignora esa línea
                        print(f"Advertencia: datos inválidos en línea ignorada -> '{linea}'")
            print(f"Inventario cargado desde '{ARCHIVO_INVENTARIO}'.")
        except FileNotFoundError:
            # Si el archivo no existe, se crea uno vacío
            print(f"Archivo '{ARCHIVO_INVENTARIO}' no encontrado. Se creará uno nuevo al agregar productos.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def __mostrar_producto(self, p):
        # Método auxiliar privado para imprimir un producto con formato uniforme
        print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")
        