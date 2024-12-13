'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''
persona = {}
while True:
    datos_pers = input("Escribe tu informacion: ").lower()
    if datos_pers == "salir":
        print("No se aceptan mas datos.")
        break
    datos = input("Escribe info para '{datos_pers}': ")