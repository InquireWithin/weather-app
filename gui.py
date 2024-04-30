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
        MainWindow.resize(491, 428)
        MainWindow.setStyleSheet("background-image: url(Background_Sky.png);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.self_submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.self_submit_button.setGeometry(QtCore.QRect(110, 290, 261, 61))
        self.self_submit_button.setMaximumSize(QtCore.QSize(261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.self_submit_button.setFont(font)
        self.self_submit_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.self_submit_button.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.self_submit_button.setStyleSheet("")
        self.self_submit_button.setIconSize(QtCore.QSize(40, 40))
        self.self_submit_button.setCheckable(False)
        self.self_submit_button.setDefault(False)
        self.self_submit_button.setFlat(False)
        self.self_submit_button.setObjectName("self_submit_button")
        self.self_submit_button.clicked.connect(self.submit)
        self.self_location_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.self_location_label.setGeometry(QtCore.QRect(0, 80, 181, 41))
        self.self_location_label.setMaximumSize(QtCore.QSize(181, 41))
        self.self_location_label.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.self_location_label.setObjectName("self_location_label")
        self.self_language_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.self_language_label.setGeometry(QtCore.QRect(0, 130, 241, 41))
        self.self_language_label.setObjectName("self_language_label")
        self.self_days_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.self_days_label.setGeometry(QtCore.QRect(0, 180, 171, 41))
        self.self_days_label.setMaximumSize(QtCore.QSize(171, 41))
        self.self_days_label.setObjectName("self_days_label")
        self.self_metric_checkbox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.self_metric_checkbox.setGeometry(QtCore.QRect(290, 230, 81, 20))
        self.self_metric_checkbox.setMaximumSize(QtCore.QSize(81, 20))
        self.self_metric_checkbox.setStyleSheet("")
        self.self_metric_checkbox.setObjectName("self_metric_checkbox")
        self.self_imperial_checkbox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.self_imperial_checkbox.setGeometry(QtCore.QRect(290, 250, 81, 20))
        self.self_imperial_checkbox.setMaximumSize(QtCore.QSize(81, 20))
        self.self_imperial_checkbox.setStyleSheet("")
        self.self_imperial_checkbox.setObjectName("self_imperial_checkbox")
        self.self_title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.self_title_label.setGeometry(QtCore.QRect(140, 0, 241, 61))
        self.self_title_label.setMaximumSize(QtCore.QSize(241, 61))
        self.self_title_label.setStyleSheet("font: 36pt \"Comic Sans MS\";")
        self.self_title_label.setObjectName("self_title_label")
        self.self_days_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.self_days_edit.setGeometry(QtCore.QRect(170, 180, 61, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.self_days_edit.setFont(font)
        self.self_days_edit.setStyleSheet("background-image: url(White Background.png);\n"
"font: 12pt \"MS Sans Serif\";")
        self.self_days_edit.setInputMask("")
        self.self_days_edit.setText("")
        self.self_days_edit.setMaxLength(1)
        self.self_days_edit.setObjectName("self_days_edit")
        self.self_location_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.self_location_edit.setGeometry(QtCore.QRect(180, 80, 221, 41))
        self.self_location_edit.setMaximumSize(QtCore.QSize(221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.self_location_edit.setFont(font)
        self.self_location_edit.setStyleSheet("background-image: url(White Background.png);\n"
"font: 12pt \"MS Sans Serif\";")
        self.self_location_edit.setMaxLength(16)
        self.self_location_edit.setObjectName("self_location_edit")
        self.self_language_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.self_language_edit.setGeometry(QtCore.QRect(240, 130, 241, 41))
        self.self_language_edit.setMaximumSize(QtCore.QSize(241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.self_language_edit.setFont(font)
        self.self_language_edit.setStyleSheet("background-image: url(White Background.png);\n"
"font: 12pt \"MS Sans Serif\";")
        self.self_language_edit.setMaxLength(2)
        self.self_language_edit.setFrame(True)
        self.self_language_edit.setClearButtonEnabled(False)
        self.self_language_edit.setObjectName("self_language_edit")
        self.self_unit_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.self_unit_label.setGeometry(QtCore.QRect(0, 230, 141, 41))
        self.self_unit_label.setObjectName("self_unit_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.self_location_edit, self.self_language_edit)
        MainWindow.setTabOrder(self.self_language_edit, self.self_days_edit)
        MainWindow.setTabOrder(self.self_days_edit, self.self_metric_checkbox)
        MainWindow.setTabOrder(self.self_metric_checkbox, self.self_imperial_checkbox)

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
		
		
