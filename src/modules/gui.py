# Classes, functions and constants for the Qt gui.

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *

# Constants
# Standard layout spacing sizes
SPACING_VERTICAL = 15
SPACING_HORIZONTAL = SPACING_VERTICAL

class MainForm(QtWidgets.QWidget):
    '''The main input widget.'''
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Podcast information
        self.podcast_source = QLineEdit()
        self.podcast_location = QLineEdit()

        # Download settings
        self.delay = QLineEdit()
        self.download_to = QLineEdit()
        self.rename = QCheckBox("Rename each file to the episode name?")

        # Download button
        self.download_button = QPushButton("Download")

        # Widget layout
        self.layout = QtWidgets.QVBoxLayout()
        
        # Add the input widgets and labels
        self.layout.addWidget(QLabel('Podcast source:'))
        self.layout.addWidget(self.podcast_source)
        self.layout.addSpacing(SPACING_VERTICAL)

        self.layout.addWidget(QLabel('Podcast location:'))
        self.layout.addWidget(self.podcast_location)
        self.layout.addSpacing(SPACING_VERTICAL)

        self.layout.addWidget(QLabel('Delay between downloads:'))
        self.layout.addWidget(self.delay)
        self.layout.addSpacing(SPACING_VERTICAL)
        
        self.layout.addWidget(QLabel('Download to:'))
        self.layout.addWidget(self.download_to)
        self.layout.addSpacing(SPACING_VERTICAL)
        
        self.layout.addWidget(self.rename)
        self.layout.addSpacing(SPACING_VERTICAL)

        self.layout.addWidget(self.download_button)
        

        #layout.addWidget(QLineEdit())
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setGeometry(QtCore.QRect())

        self.setLayout(self.layout)

        # Event listener for the download button
        self.download_button.clicked.connect(self.start_download)

    def start_download(self):
        print("Download function placeholder.")
        print(f"Downloading from {self.podcast_location.text()} to {self.download_to.text()}.")
        print()

class ProgressDisplay(QtWidgets.QWidget):
    '''The main output widget.'''

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # The output is displayed as a text box
        self.output = QtWidgets.QTextEdit()

        # Widget layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.output)
        self.setLayout(self.layout)

class MainWidget(QtWidgets.QWidget):
    '''The main GUI widget.'''

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.input_widget = MainForm(self)

        self.output_widget = ProgressDisplay(self)

        # Widget layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.input_widget)
        self.layout.addWidget(self.output_widget)

        self.setLayout(self.layout)

        self.setGeometry(10, 10, 1000, 500)
