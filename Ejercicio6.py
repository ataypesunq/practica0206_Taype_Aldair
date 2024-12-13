'''Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
Preguntar por el NIF del alumno/a y mostrar sus datos.
Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
Terminar el programa.
'''
base_datos = {}
def añadir_alumno():
    """Esta funcion añade un nuevo alumno a la base de datos."""
    nif = input("Escribe el NIF del alumno/a: ")
    # Se comprueba si el NIF ya esta registrado
    if nif in base_datos:
        print("NOF registrado.")
        return
    # Se pide los datos al usuario
    nombre = input("Escribe el nombre del alumno/a: ")
    apellidos = input("Escribe los apellidos del alumno/a: ")
    telefono = input("Escribe el teléfono del alumno/a: ")
    correo = input("Escribe el correo electrónico del alumno/a: ")
    aprobado = input("¿Está aprobado? (Sí o No): ").lower() == "sí"

    # Se crea el diccionario del alumno y lo agregamos a la base de datos usando el NIF como clave
    base_datos[nif] = {
        'nombre': nombre,
        'apellidos': apellidos,
        'telefono': telefono,
        'correo': correo,
        'aprobado': aprobado
    }
    print("Datos del alumno/a añadidos.")

def eliminar_alumno():
    "Esta funcion elimina un alumno de la base de datos"
    nif = input("Escribe el NIF del alumno/a que desea eliminar: ")
    # Se comprueba si el NIF existe en nuestra base de datos
    if nif in base_datos:
        del base_datos[nif] # Eliminamos al alumno/a
        print("Alumno/a eliminado.")
    else:
        print("Ese NIF no existe.")

def mostrar_alumno():
    "Esta funcionn muestra los datos de un alumno"
    nif = input("Escribw el NIF del alumno/a a mostrar: ")
    # Se comprueba si el NIF existe, y se muestran los datos si existe y si no, se muestra un mensaje
    if nif in base_datos:
        alumno = base_datos[nif]
        print(f"NIF: {nif}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellidos: {alumno['apellidos']}")
        print(f"Teléfono: {alumno['telefono']}")
        print(f"Correo: {alumno['correo']}")
        print(f"Aprobado: {'Sí' if alumno['aprobado'] else 'No'}")
    else:
        print("No se encontró ningún alumno/a con ese NIF.")

def listar_todo_el_alumnado():
    "Esta funcion es para listar todo el alumnado"
    if base_datos:
        print("\nLista de todo el alumnado:")
        # Se recorre la base de datos y se muestra el NIF y el nombre de cada alumno, si no esta, se muestra un mensaje
        for nif, alumno in base_datos.items():
            print(f"NIF: {nif}, Nombre: {alumno['nombre']} {alumno['apellidos']}")
    else:
        print("No hay alumnos registrados.")
        