'''Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''
diccionario = {}
print("Introduce palabras (español:inglés), utiliza comas para separar: ")
print("Escribe 'terminar' para dejar de escribir y guardar palabras.")

while True:
    entrada = input("Escribe palabras: ")
    if entrada.lower() == "terminar":
        print("Fin de diccionario.")
        break
    lista_claves_valores = entrada.split(",")
    for claves_valores in lista_claves_valores:
        if ":" in claves_valores:
            espanol, ingles = map(str.strip, claves_valores.split(":"))
            diccionario[espanol] = ingles
        else:
            print(f"Formato erróneo")
print("Diccionario:")
for clave, valor in diccionario.items():
    print(f"{espanol}: {ingles}")
frase = input("Escribe frase en español: ")

traduccion = []
for palabra in frase.split():
    traduccion.append(diccionario.get(palabra, palabra))

print("Traducción:")
print(" ".join(traduccion))
