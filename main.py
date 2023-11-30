import sys
from PySide6.QtWidgets import QApplication
from ventana import Ventana

def main():
    """Función principal de la aplicación.

    Esta función crea y configura la interfaz gráfica de la aplicación,
    mostrando una ventana principal y ejecutando el bucle principal de la aplicación.

    """
    # Crea una instancia de la aplicación de PySide6
    app = QApplication(sys.argv)

    # Crea una instancia de la ventana principal de la aplicación
    window = Ventana()

    # Muestra la ventana en la interfaz de usuario
    window.show()

    # Inicia la aplicación y entra en su bucle principal
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()  # Llama a la función main() para iniciar la aplicación