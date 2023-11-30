from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class VentanaEdicion(QDialog):
    def __init__(self, registro):
        """Inicializa la ventana de edición de registro.

        Args:
            registro (list): Una lista con los valores del registro a editar.
        """
        super().__init__()
        self.registro = registro
        self.setWindowTitle("Editar Registro")
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de usuario de la ventana de edición."""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Crea campos de edición para cada valor del registro
        self.campos_edicion = [QLineEdit(valor) for valor in self.registro]

        # Agrega los campos de edición al diseño
        for campo in self.campos_edicion:
            layout.addWidget(campo)

        # Botones para aceptar o cancelar la edición
        boton_aceptar = QPushButton("Aceptar")
        boton_cancelar = QPushButton("Cancelar")

        layout.addWidget(boton_aceptar)
        layout.addWidget(boton_cancelar)

        boton_aceptar.clicked.connect(self.accept)
        boton_cancelar.clicked.connect(self.reject)

    def obtener_datos_editados(self):
        """Obtiene los datos editados de los campos de edición.

        Returns:
            list: Una lista con los datos editados, incluyendo el DNI y la edad como un número entero.
        """
        # Agrega el valor del campo DNI a la lista de datos editados
        datos_editados = [campo.text() for campo in self.campos_edicion]

        try:
            edad = int(datos_editados[4])  # Intenta convertir la edad en un número entero
            datos_editados[4] = edad  # Reemplaza el valor de la edad con el entero obtenido
        except ValueError:
            # Si no se puede convertir la edad a un número entero, muestra un mensaje de error
            QMessageBox.warning(self, "Error", "Por favor, ingrese una edad válida como un número entero.")
            return None  # Retorna None para indicar que ocurrió un error

        return datos_editados