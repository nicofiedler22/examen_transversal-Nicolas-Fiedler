
productos = {"datos" : 
        [
             {
             '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}
        ]
}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0]
         }

def stock_marca():
    busqueda = input("Ingresa la marca que deseas consultar: ").lower()
    if busqueda == "hp":
        print("Stock disponible: 2")
    if busqueda == "lenovo":
        print("Stock disponible: 3")
    if busqueda == "asus":
        print("Stock disponible: 2")
    if busqueda == "dell":
        print("Stock disponible: 1")

def busqueda_precio():
    p_min = int(input("Ingresa el precio mínimo del producto: "))
    p_max = int(input("Ingresa el precio máximo del producto: "))
    if p_min <= 0:
        print("ERROR: El valor no puede ser negativo ni cero.")
    elif p_max <= 0:
        print("ERROR: El valor no puede ser negativo ni cero.")
    elif p_min >= 290890 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus, JjfFHD -- Asus, UWU131HD -- Dell, fgdxFHD -- HP, 8475HD -- HP, 342FHD -- Lenovo, 123FHD -- Lenovo, 2175HD -- Lenovo')
    elif p_min >= 327990 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus, JjfFHD -- Asus, UWU131HD -- Dell, fgdxFHD -- HP, 8475HD -- HP, 342FHD -- Lenovo, 2175HD -- Lenovo')
    elif p_min >= 387990 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus, JjfFHD -- Asus, fgdxFHD -- HP, 8475HD -- HP, 342FHD -- Lenovo')
    elif p_min >= 424990 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus, JjfFHD -- Asus, fgdxFHD -- HP, 342FHD -- Lenovo')
    elif p_min >= 444990 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus, UWU131HD -- Dell, fgdxFHD -- HP, 342FHD -- Lenovo')
    elif p_min >= 664990 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus, fgdxFHD -- HP')
    elif p_min >= 665000 and (p_max <= 749990):
        print('Los productos entre ese rango de precios son: GF75HD -- Asus')
    else:
        print("Producto inexistente")

def act_precio():
    while True:
        modelo = input("Ingrese el modelo que desea actualizar: ")
        if modelo == "8475HD" or (modelo == "2175HD") or (modelo == "JjfFHD") or (modelo == "fgdxFHD") or (modelo == "123FHD") or (modelo == "342FHD") or (modelo == "GF75HD") or (modelo == "UWU131HD"):
            print("")
        n_precio = int(input("Ingrese el nuevo precio: "))
        if n_precio <= 0:
            print("Error: no se permiten números negativos.")

        print("Precio actualizado!!")
        pregunta = input("¿Deseas actualizar otro precio? (sí/no): ").lower()
        if pregunta == "si":
            continue
        else:
            break

while True:
    print("*** MENÚ PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    opc = int(input("Por favor, ingresa una opción: "))

    if opc == 1:
        stock_marca()
    elif opc == 2:
        busqueda_precio()
    elif opc == 3:
        act_precio()
    elif opc == 4:
        print("Programa finalizado.")
        break