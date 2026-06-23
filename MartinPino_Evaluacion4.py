def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_stock(stock):
    return stock.isdigit() and int(stock) >= 0


def validar_precio(precio):
    try:
        return float(precio) > 0
    except:
        return False


def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. agregar producto")
    print("2. buscar producto")
    print("3. eliminar producto")
    print("4. actualizar disponibilidad")
    print("5. mostrar productos")
    print("6. salir")


def leer_opcion():
    while True:
        try:
            opcion = int(input("ingrese una opcion: "))

            if 1 <= opcion <= 6:
                return opcion
            else:
                print("debe ingresar una opción entre 1 y 6")

        except ValueError:
            print("debe ingresar un numero valido")


def agregar_producto(lista):
    nombre = input("ingrese nombre: ")

    if not validar_nombre(nombre):
        print("error: El nombre no puede estar vacio")
        return

    stock = input("ingrese stock: ")

    if not validar_stock(stock):
        print("error: El stock debe ser un entero mayor o igual a cero")
        return

    precio = input("ingrese precio: ")

    if not validar_precio(precio):
        print("error: El precio debe ser mayor que cero")
        return

    producto = {
        "nombre": nombre,
        "stock": int(stock),
        "precio": float(precio),
        "disponible": int(stock) > 0
    }

    lista.append(producto)
    print("producto registrado correctamente")


def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower():
            return i

    return -1


def actualizar_disponibilidad(lista):
    for producto in lista:
        producto["disponible"] = producto["stock"] > 0


def mostrar_productos(lista):
    actualizar_disponibilidad(lista)

    if len(lista) == 0:
        print("no existen productos registrados")
        return

    print("\n=== LISTA DE PRODUCTOS ===")

    for producto in lista:
        print(f"nombre: {producto['nombre']}")
        print(f"stock: {producto['stock']}")
        print(f"precio: {producto['precio']}")

        if producto["disponible"]:
            print("estado: DISPONIBLE")
        else:
            print("estado: SIN STOCK")

        print("*" * 45)

productos = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_producto(productos)

    elif opcion == 2:
        nombre = input("ingrese nombre a buscar: ")
        posicion = buscar_producto(productos, nombre)

        if posicion != -1:
            print("\n producto encontrado")
            print("posición:", posicion)
            print("nombre:", productos[posicion]["nombre"])
            print("stock:", productos[posicion]["stock"])
            print("precio:", productos[posicion]["precio"])

            if productos[posicion]["disponible"]:
                print("estado: DISPONIBLE")
            else:
                print("estado: SIN STOCK")
        else:
            print("el producto no existe")

    elif opcion == 3:
        nombre = input("ingrese nombre a eliminar: ")
        posicion = buscar_producto(productos, nombre)

        if posicion != -1:
            productos.pop(posicion)
            print("producto eliminado correctamente")
        else:
            print(f"el producto '{nombre}' no se encuentra registrado")

    elif opcion == 4:
        actualizar_disponibilidad(productos)
        print("disponibilidad actualizada correctamente")

    elif opcion == 5:
        mostrar_productos(productos)

    elif opcion == 6:
        print("gracias por usar el sistema. Vuelva pronto")
        break
                        
                        





