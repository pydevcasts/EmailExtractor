import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap

class ImageDisplay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Display")
        self.setGeometry(100, 100, 400, 300)

        # Create a QLabel widget to display the image
        self.image_label = QLabel(self)
        
        # Load the image using QPixmap
        pixmap = QPixmap("path/to/your/image.jpg")

        # Set the pixmap to the QLabel
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(10, 10, pixmap.width(), pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDisplay()
    window.show()
    sys.exit(app.exec())
