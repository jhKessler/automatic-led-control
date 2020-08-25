import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QColorDialog
from PyQt5.QtGui import QIcon
import PyQt5.QtCore as QtCore
import requests
import ctypes


# set up icon
myappid = 'led_controller.1.0' # version
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# change ColorDialog class
class ColorPicker(QColorDialog):

    # intialize changed color dialog class
    def __init__(self):
        super().__init__()

    # change submit and cancel button functions
    def done(self, int):
        
        # quit app if cancel is clicked
        if int == 0:
            app.quit()
        
        # change color if submit button is clicked
        else:
            win.changeColor(win.colorPicker.currentColor())


# class mainwindow
class MainWindow(QMainWindow):

    # intialize window
    def __init__(self):
        super().__init__()
        self.x, self.y = 400, 400
        self.title = 'LED-Controller'
        
        # intialize ui
        self.initUI()

    def initUI(self, firstStart=True):
        
        # create colorpicker
        self.colorPicker = ColorPicker()
        
        # set up when started for the first time
        if firstStart:
            
            # set up window
            self.width, self.height = self.colorPicker.width(), self.colorPicker.height()
            self.setGeometry(self.x, self.y, self.width, self.height)
            self.adjustSize()
            self.setWindowTitle(self.title)
            
            # show window
            self.show()

        
        else:
            
            # set color to previous value if started for second time
            self.colorPicker.setCurrentColor(newColor)

        # create new color dialog
        self.setCentralWidget(self.colorPicker)

    # change color funtion
    def changeColor(self, colorObj):
        global red, green, blue, newColor
        
        # color object for using in application
        newColor = colorObj
        
        # rgb values for changing the led color
        color = colorObj.getRgb()
        red, green, blue = color[0], color[1], color[2]
        rgb_value = (red, green, blue)

        # value file and led status file
        if rgb_value != (0, 0, 0):
            with open("values.txt", "w") as values_file:
                values_file.write(f"{red}:{green}:{blue}")
        else:
            with (r"led_status.txt", "w") as led_status_file:
                led_status_file.write("off")
        
        # change led color
        #requests.get(f"192.168.178.30/?red={red}&green{green}&blue={blue}")

        # create new color dialog widget
        self.initUI(False)

def main():
    global win, app
    
    # create application and window
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())


# start application
if __name__ == '__main__':
    main()
