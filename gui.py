import sys
#from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLineEdit, QCheckBox, QMessageBox
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import os #system calls to run go
import platform #check for windows or linux
class WeatherApp(QWidget):
#TODO: clean all non-owm stuff in config file
#TODO: remember user settings next launch
#TODO: users when they fresh download the program will not be able to request due to no API key, must be specified in .wegorc
#TODO: a better gui
#TODO: debug mode (built into engine, not added to gui)
#TODO: install script (dependency check, platform specific)
#TODO: instead of looping through config file, just state the changes and write, (remember user settings next time they launch gui, should read from config file and adjust gui elements accordingly, otherwise should use gui defaults
#TODO: wego knows your location so i should add that to the default option, gui should autofill with this location
#TODO: better locations and add states for US?
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')

        # Location selection
        self.location_label = QLabel('Select City:')
        self.location_edit = QLineEdit()
        self.location_edit.setMaxLength(16)
        
		
        # Language selection
        self.language_label = QLabel('Select Language Code:')
        self.language_edit = QLineEdit()
        self.language_edit.setMaxLength(16)

        # Days to display
        self.days_label = QLabel('Days to Display:')
        self.days_edit = QLineEdit()
        self.days_edit.setValidator(QIntValidator(1,7))
        
        # Unit selection
        self.unit_label = QLabel('Select Units:')
        self.metric_checkbox = QCheckBox('Metric')
        self.imperial_checkbox = QCheckBox('Imperial')

        # Submit button
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_edit)
        layout.addWidget(self.language_label)
        layout.addWidget(self.language_edit)
        layout.addWidget(self.days_label)
        layout.addWidget(self.days_edit)
        layout.addWidget(self.unit_label)
        layout.addWidget(self.metric_checkbox)
        layout.addWidget(self.imperial_checkbox)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit(self):
        system = platform.system()
        location = self.location_edit.text()
        language = self.language_edit.text()
        days = self.days_edit.text()
        units = []
        isMetric = 0
        if self.metric_checkbox.isChecked():
            units.append('Metric')
            isMetric=1
        if self.imperial_checkbox.isChecked():
            units.append('Imperial')
            isMetric=0
            
            
            
            
        if not language:
            QMessageBox.warning(self, 'Warning', 'Please enter a language.')
            return
        elif len(language) !=2 or not all(ord(char) < 128 for char in language):
            QMessageBox.warning(self, 'Warning', 'Please enter exactly 2 ASCII characters for language code.')
            if not days:
                QMessageBox.warning(self, 'Warning', 'Please enter the number of days to display.')
                return

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
        #assume if linux, mac, or unix-like then the config is in ~/.wegorc
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
        if system == "Windows":
            os.system("wego" + days + " " + location)
        else:
            os.system("go run main.go " + days + " " + location)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    #replace with default conf after? remember user settings?
    sys.exit(app.exec())

