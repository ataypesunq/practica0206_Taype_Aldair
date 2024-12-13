'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”.
'''
nombre = input("Cual es tu nombre?: ")
edad = int(input("Cual es tu edad?: "))
direccion = input("Cual es tu direccion?: ")
telf = (input("Cual es tu telefono?: "))
datos = {"nombre" : nombre,"edad" : edad,"direccion" : direccion,
    "telefono" : telf
}
print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}.")