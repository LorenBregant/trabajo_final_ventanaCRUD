from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from ventana_edicion import VentanaEdicion
import bbdd

class VentanaDatos(QDialog):
    def __init__(self):
        """Inicializa la ventana de datos."""
        super().__init__()
        self.setWindowTitle("Base de Datos")
        self.setMinimumSize(550, 400)
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de usuario de la ventana de datos."""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Cuadro de búsqueda por ID
        self.cuadro_busqueda_id = QLineEdit()
        self.cuadro_busqueda_id.setPlaceholderText("Buscar por ID...")
        self.cuadro_busqueda_id.textChanged.connect(self.filtrar_tabla)
        layout.addWidget(self.cuadro_busqueda_id)

        # Cuadro de búsqueda por DNI
        self.cuadro_busqueda_dni = QLineEdit()
        self.cuadro_busqueda_dni.setPlaceholderText("Buscar por DNI...")
        self.cuadro_busqueda_dni.textChanged.connect(self.filtrar_tabla)
        layout.addWidget(self.cuadro_busqueda_dni)

        # Cuadro de búsqueda por Apellido
        self.cuadro_busqueda_apellido = QLineEdit()
        self.cuadro_busqueda_apellido.setPlaceholderText("Buscar por Apellido...")
        self.cuadro_busqueda_apellido.textChanged.connect(self.filtrar_tabla)
        layout.addWidget(self.cuadro_busqueda_apellido)

        # Crea una tabla para mostrar los datos
        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)

        # Agrega los encabezados de las columnas (opcional)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "DNI", "Edad"])

        # Botón para cerrar la ventana
        boton_cerrar = QPushButton("Cerrar")
        layout.addWidget(boton_cerrar)
        boton_cerrar.clicked.connect(self.close)

        # Botones de editar y eliminar
        boton_editar = QPushButton("Editar")
        boton_eliminar = QPushButton("Eliminar")

        # Cuadro horizontal para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(boton_editar)
        botones_layout.addWidget(boton_eliminar)
        layout.addLayout(botones_layout)

        # Conecta la señal textChanged de los cuadros de búsqueda a la función de búsqueda en tiempo real
        self.cuadro_busqueda_id.textChanged.connect(self.filtrar_tabla)
        self.cuadro_busqueda_dni.textChanged.connect(self.filtrar_tabla)
        self.cuadro_busqueda_apellido.textChanged.connect(self.filtrar_tabla)

        # Conecta la señal itemSelectionChanged de la tabla a la función de selección
        self.tabla.itemSelectionChanged.connect(self.seleccionar_registro)

        # Conecta los botones de editar y eliminar a las funciones correspondientes
        boton_editar.clicked.connect(self.editar_registro)
        boton_eliminar.clicked.connect(self.eliminar_registro)

        # Cargamos los datos desde la base de datos al inicializar
        self.cargar_datos_desde_bd()

    def cargar_datos_desde_bd(self):
        """Carga los datos desde la base de datos y actualiza la tabla."""
        self.datos = bbdd.obtener_datos_desde_bd()
        self.actualizar_tabla()

    def actualizar_tabla(self):
        """Actualiza la tabla con los datos cargados desde la base de datos."""
        self.tabla.clearContents()
        self.tabla.setRowCount(0)
        self.tabla.setColumnCount(0)

        if not self.datos:
            return

        self.tabla.setRowCount(len(self.datos))
        self.tabla.setColumnCount(len(self.datos[0]))

        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "DNI", "Edad"])

        for fila, datos_fila in enumerate(self.datos):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Deshabilita la edición de celdas
                self.tabla.setItem(fila, columna, item)

    def filtrar_tabla(self):
        """Filtra la tabla según el ID o DNI especificado en los cuadros de búsqueda."""
        filtro_id = self.cuadro_busqueda_id.text().strip()
        filtro_dni = self.cuadro_busqueda_dni.text().strip()
        filtro_apellido = self.cuadro_busqueda_apellido.text().strip()

        for fila in range(self.tabla.rowCount()):
            texto_id = self.tabla.item(fila, 0).text()
            texto_dni = self.tabla.item(fila, 3).text()
            texto_apellido = self.tabla.item(fila, 2).text()

            # Verifica si el texto de ID o DNI contiene el filtro
            if (filtro_id and texto_id.startswith(filtro_id)) or (filtro_dni and filtro_dni in texto_dni) or (filtro_apellido.capitalize() and filtro_apellido.capitalize() in texto_apellido):
                self.tabla.setRowHidden(fila, False)
            else:
                self.tabla.setRowHidden(fila, True)

        # Si ambos cuadros de búsqueda están vacíos, mostrar todos los registros
        if not filtro_id and not filtro_dni and not filtro_apellido:
            for fila in range(self.tabla.rowCount()):
                self.tabla.setRowHidden(fila, False)

    def seleccionar_registro(self):
        """Guarda los datos de la fila seleccionada en self.registro_seleccionado."""
        filas_seleccionadas = self.tabla.selectedItems()

        if filas_seleccionadas:
            fila_seleccionada = filas_seleccionadas[0].row()
            self.registro_seleccionado = [self.tabla.item(fila_seleccionada, columna).text() for columna in range(self.tabla.columnCount())]

    def editar_registro(self):
        if hasattr(self, 'registro_seleccionado'):
            ventana_edicion = VentanaEdicion(self.registro_seleccionado)
            resultado = ventana_edicion.exec_()
            if resultado == QDialog.Accepted:
                datos_editados = ventana_edicion.obtener_datos_editados()
                if datos_editados is not None:  # Comprueba si los datos editados son válidos
                    id_registro = self.registro_seleccionado[0]

                    # Capitaliza los valores editados antes de guardarlos
                    datos_editados = [valor.capitalize() if isinstance(valor, str) else valor for valor in datos_editados]

                    # Capitaliza nombres y apellidos compuestos
                    for i in range(len(datos_editados)):
                        if isinstance(datos_editados[i], str):
                            datos_editados[i] = ' '.join(part.capitalize() for part in datos_editados[i].split())

                    # Llama a la función de bbdd para modificar el registro con los datos editados
                    bbdd.modificar_registro(id_registro, datos_editados)

                    self.cargar_datos_desde_bd()
                    self.actualizar_tabla()  # Actualiza la tabla después de la edición

    def eliminar_registro(self):
        """Elimina un registro de la base de datos y actualiza la tabla."""
        if hasattr(self, 'registro_seleccionado'):
            confirmacion = QMessageBox.question(self, "Eliminar Registro", "¿Estás seguro de que deseas eliminar este registro?",
                                            QMessageBox.Yes | QMessageBox.No)
            if confirmacion == QMessageBox.Yes:
                id_registro = self.registro_seleccionado[0]

                bbdd.eliminar_registro(id_registro)

                self.cargar_datos_desde_bd()

                for i, datos_fila in enumerate(self.datos):
                    if datos_fila[0] == id_registro:
                        del self.datos[i]
                        break

                self.cargar_datos_desde_bd()

                self.actualizar_tabla()

                self.tabla.removeRow(self.tabla.currentRow())