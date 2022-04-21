# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    # Configura la conexión
    host="localhost",
    user="",
    passwd=""
)


def initDB():
    cursor = mydb.cursor()
    cursor.execute('CREATE SCHEMA IF NOT EXISTS python')
    cursor.execute('USE python')
    # Crea las tablas correspondientes al diagrama notas.png


def muestraMenu():
    print('------- MENU -------')
    print('  1. Crear usuario')
    print('  2. Login')
    print('  3. Salir')
    print('--------------------')

def muestraOperaciones(usuario):
    print(f'------- OPERACIONES ({usuario}) -------')
    print('  1. Crear nota')
    print('  2. Listar mis notas')
    print('  3. Filtrar notas por fechas')
    print('  4. Borrar nota')
    print('  5. Logout')
    print('--------------------')


def crearUsuario():

    cursor = mydb.cursor()

    print('------ Registro de usuario ------\n')
    username =  input('Nombre de usuario : ')
    password =  input('Contraseña (¡visible!) : ')

    # Añadir el usuario a la BD

    print('------ Usuario añadido ------\n')

def login():
    username = input("Login: ")
    password = input("Password (¡visible!): ")

    # Comprobar que las credenciales son válidas
    credencialesValidas = ...

    # Si las credenciales son válidas, accedemos al meno principal
    if credencialesValidas:
        opcion = 0
        while opcion != 5:
            muestraOperaciones(username)
            opcion = int(input("Elige una opción : "))
            if opcion == 1:
                crearNota(username)
            elif opcion == 2:
                listarNotas(username)
            elif opcion == 3:
                filtrarNotas(username)
            elif opcion == 4:
                borrarNota(username)

def crearNota(username):
    titulo = input("Titulo: ")
    texto = input("Cuerpo: ")

    # Guardar nota en la BD

def listarNotas(username):
    # Mostrar por pantalla las notas del usuario, ordenadas por fecha de creación decreciente
    pass

def filtrarNotas(username):
    # Mostrar por pantalla las notas del usuario creadas entre dos fechas pedidas por pantalla
    pass

def borrarNota(username):
    # Pide el id de la nota que se quiere borrar y se elimina la fila correspondiente, siempre que la nota sea del usuario <username>
    pass

def run():
    n = 0
    while n != 3:
        muestraMenu()
        n = int(input("Elige una opción : "))
        if n == 1:
            crearUsuario()
        elif n == 2:
            login()
        elif n == 3:
            print('----- ¡Hasta pronto! -----')


if __name__ == '__main__':
    initDB()
    run()
