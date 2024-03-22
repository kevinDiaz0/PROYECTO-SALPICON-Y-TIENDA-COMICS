import random

print("***BIENVENIDOS A TIENDA COMICS***")
print("*********************************")

class Producto:
    def __init__(self, nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia):
        self.id = random.randint(1, 100)
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.pais = pais
        self.unidades = unidades
        self.garantia = garantia

inventario = []

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    ubicacion = input("Ingrese la ubicación en la tienda (A, B, C o D): ").upper()

 
    cantidad_productos_ubicacion = sum(1 for producto in inventario if producto.ubicacion == ubicacion)
    if cantidad_productos_ubicacion >= 50:
         print("Error: La ubicación ya tiene 50 productos registrados.")
         return

    descripcion = input("Ingrese la descripción del producto: ")
    casa = input("Ingrese la casa a la que pertenece el producto (Marvel, DC, etc): ")
    referencia = input("Ingrese la referencia del producto: ")
    pais = input("Ingrese el país de origen del producto: ")
    unidades = int(input("Ingrese el número de unidades compradas del producto: "))
    garantia = input("¿El producto tiene garantía extendida? (true/false): ").lower() == "true"

 
    producto = Producto(nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia)
    inventario.append(producto)
    print("Producto registrado con éxito.")

    def restar_producto_ubicacion(ubicacion):
     for producto in inventario:
        if producto.ubicacion == ubicacion:
            producto.unidades -= 1
            break


def mostrar_productos():
    if inventario:
        print("Productos en bodega:")
        for producto in inventario:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Descripción: {producto.descripcion}")
    else:
        print("No hay productos en bodega.")

def buscar_producto_por_nombre():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in inventario:
        if producto.nombre.lower() == nombre_buscar.lower():
            encontrado = True
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Descripción: {producto.descripcion}")
    if not encontrado:
        print("No se encontró el producto en el inventario.")

def modificar_unidades_compradas():
    nombre_buscar = input("Ingrese el nombre del producto cuyas unidades compradas desea modificar: ")
    encontrado = False
    for producto in inventario:
        if producto.nombre.lower() == nombre_buscar.lower():
            encontrado = True
            nuevas_unidades = int(input(f"Ingrese el nuevo número de unidades compradas para {producto.nombre}: "))
            if nuevas_unidades <= producto.unidades:
                producto.unidades = nuevas_unidades
                print("Número de unidades compradas actualizado con éxito.")
            else:
                print("Error: El nuevo número de unidades compradas no puede ser mayor al número inicial.")
    if not encontrado:
        print("No se encontró el producto en el inventario.")

def eliminar_producto():
    nombre_buscar = input("Ingrese el nombre del producto que desea eliminar: ")
    confirmacion = input(f"¿Está seguro que desea eliminar {nombre_buscar}? (sí/no): ").lower()
    if confirmacion == "sí":
        global inventario
        for producto in inventario:
            if producto.nombre.lower() == nombre_buscar.lower():
                inventario.remove(producto)
                print("Producto eliminado del inventario.")
                break
            else:
                print("No se encontró el producto en el inventario.")

def menu():
    while True:
        print("\n-- Menú --")
        print("1. Registrar un producto")
        print("2. Mostrar todos los productos en bodega")
        print("3. Buscar producto por nombre")
        print("4. Modificar número de unidades compradas")
        print("5. Eliminar un producto del inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto_por_nombre()
        elif opcion == "4":
            modificar_unidades_compradas()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()

print("***GRACIAS POR TU COMPRA***")
