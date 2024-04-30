import os
import platform
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Weather App")
        MainWindow.setStyleSheet("background-image: url(Background_Sky.png);")

        central_layout = QtWidgets.QVBoxLayout()
        central_layout.setContentsMargins(10, 10, 10, 10)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(central_layout)

        self.self_title_label = QtWidgets.QLabel("WEATHER-APP")
        self.self_title_label.setStyleSheet("font: 20pt \"Comic Sans MS\";")
        self.self_title_label.setAlignment(QtCore.Qt.AlignHCenter)
        central_layout.addWidget(self.self_title_label)

        form_layout = QtWidgets.QFormLayout()

        self.self_location_label = QtWidgets.QLabel("Select a City:")
        self.self_location_edit = QtWidgets.QLineEdit()
        form_layout.addRow(self.self_location_label, self.self_location_edit)

        self.self_language_label = QtWidgets.QLabel("Select Language:")
        self.self_language_edit = QtWidgets.QLineEdit()
        form_layout.addRow(self.self_language_label, self.self_language_edit)

        self.self_days_label = QtWidgets.QLabel("Number of Days:")
        self.self_days_edit = QtWidgets.QLineEdit()
        form_layout.addRow(self.self_days_label, self.self_days_edit)

        self.self_unit_label = QtWidgets.QLabel("Select Unit:")
        self.self_metric_checkbox = QtWidgets.QCheckBox("Metric")
        self.self_imperial_checkbox = QtWidgets.QCheckBox("Imperial")

        unit_layout = QtWidgets.QHBoxLayout()
        unit_layout.addWidget(self.self_metric_checkbox)
        unit_layout.addWidget(self.self_imperial_checkbox)

        form_layout.addRow(self.self_unit_label, unit_layout)

        central_layout.addLayout(form_layout)

        self.self_submit_button = QtWidgets.QPushButton("SUBMIT")
        self.self_submit_button.setMaximumWidth(261)
        self.self_submit_button.clicked.connect(self.submit)
        central_layout.addWidget(self.self_submit_button, alignment=QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.self_submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.self_location_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Select a City:</span></p></body></html>"))
        self.self_language_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Select Language:</span></p></body></html>"))
        self.self_days_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Number of Days:</span></p></body></html>"))
        self.self_metric_checkbox.setText(_translate("MainWindow", "Metric"))
        self.self_imperial_checkbox.setText(_translate("MainWindow", "Imperial"))
        self.self_title_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">WEATHER-APP</span></p></body></html>"))
        self.self_unit_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Select Unit:</span></p></body></html>"))
   
   #checks after submit button is hit 
    def submit(self):
       system = platform.system()
       units = []
       isMetric=0
       location = self.self_location_edit.text()
       language = self.self_language_edit.text()
       days = self.self_days_edit.text()
       if self.self_metric_checkbox.isChecked():
            units.append('Metric')
            isMetric=1
       if self.self_imperial_checkbox.isChecked():
            units.append('Imperial')
            isMetric=0
       if not language:
            QMessageBox.warning(self, 'Warning', 'Please enter a language.')
            return
       if len(language) !=2 or not all(ord(char) < 128 for char in language):
           QMessageBox.warning(self, 'Warning', 'Please enter exactly 2 ASCII characters for language code.')

       days_int = int(days)
       if days_int < 1 or days_int > 7:
           QMessageBox.warning(self, 'Warning', 'Please enter a number between 1 and 7 for days to display.')
           return

       if len(units) == 0:
           QMessageBox.warning(self, 'Warning', 'Please select either Metric or Imperial units.')
           return
       elif len(units) > 1:
           QMessageBox.warning(self, 'Warning', 'Please select only one unit system.')
           return     
       print(f"Location: {location}, Language: {language}, Days: {days}, Units: {units[0]}")
       #within the submit subroutine, a command should be issued to the engine corresponding with the user's preferences in the GUI
        #config file changes, i assume its in home dir. could add a check later to see if it was changed
        #windows home dir check
       print("Platform = " + system)
       if system == "Windows":
           home_dir = os.path.expanduser("~")
           os.chdir(home_dir)
           #file_path = home_dir + "\\.wegorc"
           file_path = ".wegorc"
        #assume if linux, mac, or unix-like then the config is in ~/.wegorc (could place it elsewhere?, dont want to clutter user home)
       else:
           file_path = os.path.expanduser("~/.wegorc")
        #easy but messy way to achieve changes that cant be done on CLI is actually just changing the config file
        #I should reset it back to defaults after the program runs or just add the functionality directly
       temp_file_path = ".wegorc_temp"
        #open orig file
     
        
       with open(file_path, 'r') as file:
           lines = file.readlines()
        	
        
       with open(temp_file_path, 'w') as temp_file:
            #temp_file.write(api-key)
           for line in lines:
        		#check for units=
               if line.strip().startswith("units="):
        			#replace with user preference
                   if isMetric==1:
                       temp_file.write("units=metric\n")
                   else:
                       temp_file.write("units=imperial\n")
        		#check for lang
               if line.strip().startswith("owm-lang="):
        		    #replace with user preference
                   lang_pref = f"owm-lang={language}\n"
                   temp_file.write(lang_pref)
               else:
                   temp_file.write(line)
        			
       os.replace(temp_file_path, file_path)
       print(".wegorc was successfully edited")
        #can probably do the same thing regardless of platform, linux should allow running 'wego' after installing via go but doesn't sometimes, maybe needs path updates?
       if system == "Windows":
           os.system("wego" + days + " " + location)
       else:
           os.system("go run main.go " + days + " " + location)
        
if __name__ == '__main__':
		app = QApplication(sys.argv)
		weather_app = Ui_MainWindow()
		weather_app.show()
		sys.exit(app.exec)
		
		
