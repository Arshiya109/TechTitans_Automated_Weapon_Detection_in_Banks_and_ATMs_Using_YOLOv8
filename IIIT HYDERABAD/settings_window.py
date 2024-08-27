from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from detection_window import DetectionWindow

# Manages the settings window
class SettingsWindow(QMainWindow):
    def __init__(self, token, location, receiver):
        super(SettingsWindow, self).__init__()
        loadUi('UI/settings_window.ui', self)
        
        self.token = token
        self.location = location
        self.receiver = receiver

        self.detection_window = DetectionWindow()

        self.pushButton.clicked.connect(self.go_to_detection)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")
        self.popup.setText("Fields must not be empty.")


    def displayInfo(self):
        self.show()

    def go_to_detection(self):
        if self.location_input.text() == '' or self.sendTo_input.text() == '':
            self.popup.exec_()
        else:
            if self.detection_window.isVisible():
                print('Detection window is already open!')
            else:
                self.detection_window.create_detection_instance(self.token, self.location, self.receiver)
                self.detection_window.start_detection()
    
    def closeEvent(self, event):
        if self.detection_window.isVisible():
            self.detection_window.detection.running = False
            self.detection_window.close()
            event.accept()