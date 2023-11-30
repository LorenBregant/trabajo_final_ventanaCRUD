import mysql.connector

# Establecer la conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ventana_pyside"  # Reemplaza con el nombre de tu base de datos
)

def obtener_datos_desde_bd():
    '''Obtiene datos desde la base de datos.

    Realiza una consulta SQL para obtener todos los registros de la tabla "personas" en la base de datos.

    Returns:
        list: Una lista de tuplas que contiene los datos de personas (nombre, apellido, edad, dni).
    '''
    try:
        cursor = mydb.cursor()

        # Realizar una consulta para obtener los datos de la base de datos
        consulta = "SELECT * FROM personas"
        cursor.execute(consulta)

        # Obtener todos los registros de la consulta
        datos = cursor.fetchall()

        cursor.close()
        return datos
    except mysql.connector.Error as error:
        print(f"Error al obtener datos desde la base de datos: {error}")
        return []

def modificar_registro(id_registro, nuevos_datos):
    '''Modifica un registro en la base de datos.

    Args:
        id_registro (int): El ID del registro que se va a modificar.
        nuevos_datos (tuple): Una tupla con los nuevos datos (nombre, apellido, edad, dni).
    '''
    try:
        cursor = mydb.cursor()

        # Actualizar el registro en la base de datos
        consulta = "UPDATE personas SET nombre = %s, apellido = %s, dni = %s, edad = %s WHERE id = %s"
        cursor.execute(consulta, (nuevos_datos[1], nuevos_datos[2], nuevos_datos[3], nuevos_datos[4], id_registro))

        mydb.commit()
        cursor.close()
    except mysql.connector.Error as error:
        print(f"Error al modificar registro: {error}")

def eliminar_registro(id_registro):
    '''Elimina un registro de la base de datos.

    Args:
        id_registro (int): El ID del registro que se va a eliminar.
    '''
    try:
        cursor = mydb.cursor()

        # Eliminar el registro de la base de datos
        consulta = "DELETE FROM personas WHERE id = %s"
        cursor.execute(consulta, (id_registro,))

        mydb.commit()
        cursor.close()
    except mysql.connector.Error as error:
        print(f"Error al eliminar registro: {error}")

def guardar_registro_en_bd(nombre, apellido, edad, dni):
    '''Guarda un nuevo registro en la base de datos.

    Args:
        nombre (str): El nombre de la persona.
        apellido (str): El apellido de la persona.
        edad (int): La edad de la persona.
        dni (str): El DNI de la persona.
    '''
    try:
        cursor = mydb.cursor()

        # Insertar un nuevo registro en la base de datos
        consulta = "INSERT INTO personas (nombre, apellido, edad, dni) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (nombre, apellido, edad, dni))

        mydb.commit()
        cursor.close()
    except mysql.connector.Error as error:
        print(f"Error al guardar registro en la base de datos: {error}")