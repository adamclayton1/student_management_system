import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, \
    QLineEdit, QPushButton, QComboBox
from datetime import datetime


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        #Create Widgets
        distance_label = QLabel('Distance')
        self.distance_line_edit = QLineEdit()


        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()
        calculate_button = QPushButton('Calculate Speed')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        # Add Widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2 )
        self.setLayout(grid)

    def calculate_speed(self):
        distance = int(self.distance_line_edit.text())
        Time = int(self.time_line_edit.text())
        speed = distance / Time
        if self.combo.currentText() == 'Metric (km)':
            unit = "KM per Hour"
        if self.combo.currentText() == 'Imperial (miles)':
            unit = "Miles Per Hour"

        self.output_label.setText(f"Average Speed: {speed}{unit}")

App = QApplication(sys.argv) #sys is standard library
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(App.exec())