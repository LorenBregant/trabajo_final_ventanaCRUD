import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
import mysql.connector
import re

from persona import Persona
from ventana_datos import VentanaDatos

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

        # Configurar la conexión a la base de datos
        self.conexion = self.conectar_mysql()
        self.crear_tabla_personas()

        # Inicializar la ventana de datos
        self.ventana_datos = VentanaDatos()
        self.ventana_datos.cargar_datos_desde_bd()
        self.ventana_datos.actualizar_tabla()
        self.setWindowTitle("Ingreso de Datos")

    def inicializar_ui(self):
        self.setGeometry(100, 100, 500, 350)
        self.crearCamposDeEntrada()
        self.crearBotones()

    def crearCamposDeEntrada(self):
        self.frame_entradas = QFrame(self)
        self.setCentralWidget(self.frame_entradas)

        layout_entradas = QVBoxLayout(self.frame_entradas)
        layout_entradas.setAlignment(Qt.AlignTop)

        self.label_nombre = self.crearEtiqueta("Ingresa tu nombre:")
        self.label_apellido = self.crearEtiqueta("Ingresa tu apellido:")
        self.label_dni = self.crearEtiqueta("Ingresa tu DNI (sin puntos):")
        self.label_edad = self.crearEtiqueta("Ingresa tu edad:")

        self.entrada_nombre = self.crearCampoDeEntrada()
        self.entrada_apellido = self.crearCampoDeEntrada()
        self.entrada_dni = self.crearCampoDeEntrada()
        self.entrada_edad = self.crearCampoDeEntrada()

        layout_entradas.addWidget(self.label_nombre)
        layout_entradas.addWidget(self.entrada_nombre)
        layout_entradas.addWidget(self.label_apellido)
        layout_entradas.addWidget(self.entrada_apellido)
        layout_entradas.addWidget(self.label_dni)
        layout_entradas.addWidget(self.entrada_dni)
        layout_entradas.addWidget(self.label_edad)
        layout_entradas.addWidget(self.entrada_edad)

    def crearEtiqueta(self, texto):
        etiqueta = QLabel(self.frame_entradas)
        etiqueta.setText(texto)
        etiqueta.setAlignment(Qt.AlignCenter)
        return etiqueta

    def crearCampoDeEntrada(self):
        campo = QLineEdit(self.frame_entradas)
        return campo

    def crearBotones(self):
        self.boton_crear = QPushButton("Crear")
        self.boton_mostrar_datos = QPushButton("Mostrar Datos")

        self.boton_crear.clicked.connect(self.crearPersonaYMostrar)
        self.boton_mostrar_datos.clicked.connect(self.mostrar_datos)

        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.boton_crear)
        layout_botones.addWidget(self.boton_mostrar_datos)

        self.frame_entradas.layout().addLayout(layout_botones)

    def conectar_mysql(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="ventana_pyside"
            )
            return conexion
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error de MySQL: {err}")
            sys.exit()

    def crear_tabla_personas(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(25) NOT NULL,
                apellido VARCHAR(25) NOT NULL,
                dni VARCHAR(12) NOT NULL,
                edad INT NOT NULL
            )
        """)
        self.conexion.commit()
        cursor.close()

    def cargar_datos(self):
        datos = []
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, apellido, dni, edad FROM personas")
        for nombre, apellido, dni, edad in cursor.fetchall():
            datos.append((nombre, apellido, dni, edad))
        cursor.close()

        if self.ventana_datos is not None:
            self.ventana_datos.datos = datos
            self.ventana_datos.actualizar_tabla()

    def guardar_datos(self, nombre, apellido, dni, edad):
        cursor = self.conexion.cursor()

        # Validar los datos antes de intentar la inserción
        if len(nombre) > 25:
            QMessageBox.warning(self, "Error", "El nombre es demasiado largo. Debe tener 25 caracteres o menos.")
        elif len(apellido) > 25:
            QMessageBox.warning(self, "Error", "El apellido es demasiado largo. Debe tener 25 caracteres o menos.")
        elif len(dni) > 8:
            QMessageBox.warning(self, "Error", "El DNI es demasiado largo. Debe tener 8 caracteres.")
        elif edad < 0 or edad > 120:
            QMessageBox.warning(self, "Error", "La edad no puede ser un valor negativo o superar el límite.")
        else:
            try:
                # Formatea el DNI con puntos como separadores de miles si no los tiene
                dni_formateado = "{:,}".format(int(dni)).replace(",", ".")

                cursor.execute("INSERT INTO personas (nombre, apellido, dni, edad) VALUES (%s, %s, %s, %s)",
                            (nombre, apellido, dni_formateado, edad))
                self.conexion.commit()
                cursor.close()

                if self.ventana_datos is not None:
                    self.ventana_datos.cargar_datos_desde_bd()
                    self.ventana_datos.actualizar_tabla()

            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Error", f"Error al guardar registro en la base de datos: {error}")
    
    def mostrar_datos(self):
        try:
            if self.ventana_datos is None:
                self.ventana_datos = VentanaDatos()
            
            self.ventana_datos.actualizar_tabla()
            self.ventana_datos.cargar_datos_desde_bd()
            

            self.ventana_datos.exec_()
        except mysql.connector.Error as error:
            QMessageBox.warning(self, "Error", f"Error de MySQL: {error}")

    def crearPersonaYMostrar(self):
        nombre = self.entrada_nombre.text()
        apellido = self.entrada_apellido.text()
        dni = self.entrada_dni.text()
        edad = self.entrada_edad.text()

        try:
            edad = int(edad)
            if edad <= 0:
                raise ValueError("Edad negativa no válida.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una edad válida.")
            return

        if not nombre or not apellido or not dni.isnumeric() or len(dni) != 8:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un nombre, apellido y DNI válidos.")
            return
        
        # Validar que el nombre y apellido contengan solo letras y espacios
        if not re.match(r'^[A-Za-z ]*$', nombre) or not re.match(r'^[A-Za-z ]*$', apellido):
            QMessageBox.warning(self, "Error", "El nombre y el apellido solo deben contener letras.")
            return

        # Capitalizar nombres o apellidos compuestos.
        nombre = ' '.join(part.capitalize() for part in nombre.split())
        apellido = ' '.join(part.capitalize() for part in apellido.split())

        if self.verificar_dni_existente(dni):
            QMessageBox.warning(self, "Error", "El DNI ya se encuentra registrado.")
            return

        persona = Persona(nombre, apellido, dni, edad)

        mensaje = f"Nombre completo: {persona.obtener_nombre_completo()}\nDNI: {persona.obtener_dni()}\nEdad: {persona.obtener_edad()}"
        QMessageBox.information(self, "Información de la Persona", mensaje)

        self.guardar_datos(nombre, apellido, dni, edad)

        if self.ventana_datos is not None:
            self.ventana_datos.cargar_datos_desde_bd()
            self.ventana_datos.actualizar_tabla()

        self.entrada_nombre.clear()
        self.entrada_apellido.clear()
        self.entrada_dni.clear()
        self.entrada_edad.clear()

    def verificar_dni_existente(self, dni):
        # Formatea el DNI ingresado para que coincida con el formato almacenado en la base de datos
        dni_formateado = "{:,}".format(int(dni)).replace(",", ".")

        cursor = self.conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM personas WHERE dni = %s", (dni_formateado,))
        count = cursor.fetchone()[0]
        cursor.close()
        return count > 0