'''Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.
Producto      Precio
Pan             1.40
Huevos          2.30
Cebolla         0.85
Aceite          4.35
'''
lista_compra = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
producto = input("Que quiere comprar(Pan, Huevos, Cebolla, Aceite): ")
num_ud = float(input("Cuantas unidades: "))
if producto in lista_compra:
    precio_total = num_ud * lista_compra[producto]
    print(f"El precio es: {precio_total}.")
else:
    print(f"No tenemos ese producto")