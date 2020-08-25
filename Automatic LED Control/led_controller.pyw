import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QColorDialog
import PyQt5.QtCore
import requests

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.x, self.y = 400, 400
        self.title = 'LED-Controller'
        self.initUI()

    def initUI(self, firstStart=True):
        self.colorPicker = QColorDialog()
        if firstStart:
            self.width, self.height = self.colorPicker.width(), self.colorPicker.height()
            self.setGeometry(self.x, self.y, self.width, self.height)
            self.adjustSize()
            self.setWindowTitle(self.title)
            self.show()
        else:
            self.colorPicker.setCurrentColor(newColor)

        self.setCentralWidget(self.colorPicker)
        self.colorPicker.colorSelected.connect(lambda: self.changeColor(self.colorPicker.currentColor()))


    def changeColor(self, colorObj):
        global red, green, blue, newColor

        newColor = colorObj
        color = colorObj.getRgb()
        red, green, blue = color[0], color[1], color[2]
        rgb_value = (red, green, blue)
        if rgb_value != (0, 0, 0):
            with open("values.txt", "w") as values_file:
                values_file.write(f"{red}:{green}:{blue}")
        else:
            with ("led_status.txt", "w") as led_status_file:
                led_status_file.write("off")

        #requests.get(f"192.168.178.30/?red={red}&green{green}&blue={blue}")
        self.initUI(False)

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
