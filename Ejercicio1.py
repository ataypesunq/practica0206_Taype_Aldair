'''Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
x = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Escriba la divisa(Euro, Dollar, Yen): ")
if divisa in x:
    print(f"{divisa} corresponde a: {x[divisa]}.")
else:
    print(f"{divisa} no está en el diccionario.")