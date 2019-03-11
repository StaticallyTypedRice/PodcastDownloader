# Classes, functions and constants for the Qt gui.

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *

# Constants
# Standard layout spacing sizes
SPACING_VERTICAL = 15
SPACING_HORIZONTAL = SPACING_VERTICAL

class ParallelWidgets(QtWidgets.QWidget):
    '''Places two or more widgets in parallel horizontally (side by side).
    
    Arguments:
     - This class should be initialized with each widget as its own argument,
       in order from left to right
       Example: ParallelWidgets(QWidgetLeft(), QWidgetRight())
    '''

    def __init__(self, *args, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.layout = QtWidgets.QHBoxLayout()

        # Add each widget to the horizontal box
        for a in args:
            self.layout.addWidget(a)

        self.setLayout(self.layout)

class MainForm(QtWidgets.QWidget):
    '''The main input widget.'''
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Podcast information
        self.podcast_source = QLineEdit()
        self.podcast_location = QLineEdit()
        #self.podcast_location.setText("http://")

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

        required_fields = [self.podcast_location, self.download_to]
        number_fields = [self.delay]

        validate_required = validate_required_fields(required_fields)
        validate_numbers = validate_number_fields(number_fields, integer=True, min=(0, True))

        # Highlight invalid fields
        if not validate_required['valid']:
            i = 0
            for field in validate_required['fields']:
                if not field:
                    highlight_invalid_field(required_fields[i])
                i += 1
        if not validate_numbers['valid']:
            i = 0
            for field in validate_numbers['fields']:
                if not field[0]:
                    highlight_invalid_field(number_fields[i])
                i += 1

        # Download the files if all fields are valid
        if validate_required['valid']:
            print(f"Downloading from {self.podcast_location.text()} to {self.download_to.text()}.")
            #TODO

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

# Functions
def validate_required_fields(widgets: list) -> dict:
    '''Checks that all reqired fields are filled.

    Returns a dict with two variables:
     - valid: True if and only if all fields are valid
     - fields: A list of booleans corresponding to the validity of each field

    Arguments:
     - widgets: a list of text field widget objects
    '''

    # This variable will be set to false if any fields are invalid
    valid = True

    # List whether each field is valid
    # in the order as they were passed as arguments
    fields = []

    for w in widgets:
        if not w.text():
            # Set 'valid' to false if a field is empty
            valid = False

            # Record the validity of the field
            fields.append(False)
        else:
            # Record the validity of the field
            fields.append(True)

    return {
        'valid': valid,
        'fields': fields,
    }

def validate_number_fields(widgets: list, integer: bool=False, max: tuple=(None, True),
                           min: tuple=(None, True)) -> dict:
    '''Checks that number fields are valid.

    Returns a dict with two variables:
     - valid: True if and only if all fields are valid

     - fields: A list of tuples corresponding each field, where the first value is the
               validity and the second value is a list of strings for the reasons it is
               invalid. See the error strings section.

    Error strings:
     - 'not_a_number'
     - 'not_an_integer'
     - 'too_large'
     - 'too_small'

    Arguments:
     - widgets: a list of text field widget objects

     - integer: if true, the fields will only accept integers

     - max: a tuple where the first value is the maximum acceptable number and
            the second value is a boolean of whether the maximum number
            should be accepted. Use None as the first value for an unlimited range.

     - max: a tuple where the first value is the maximum acceptable number and
            the second value is a boolean of whether the maximum number
            should be accepted. Use None as the first value for an unlimited range.

    Examples:
     - Accepts positive integers:
        validate_number_fields(field, integer=True, max=(None, True), min=(0, False))

     - Accepts negative integers:
        validate_number_fields(field, integer=True, max=(0, False), min=(None, True))

     - Accepts positive integers and zero:
        validate_number_fields(field, integer=True, max=(None, True), min=(0, True))
    '''

    # This variable will be set to false if any fields are invalid
    valid = True

    # List whether each field is valid
    # in the order as they were passed as arguments
    fields = []

    for w in widgets:
        # This variable will be set to false if the current field is invalid
        field_valid = True

        # Keep track of the errors
        errors = []

        # Check that the value is a number
        # The other checks are in this try-catch block because they will all fail
        # the input is not a number.
        try:
            # Try to convert the string to a float
            number = float(w.text())

            # Check that the value is an integer if applicable
            if integer:
                try:
                    int(number)
                except:
                    field_valid = False
                    errors.append('not_an_integer')

            # Check that the value is not too large is applicable
            if max[0] is not None:
                if max[1]:
                    # The maximum value is acceptable
                    if not number <= max[0]:
                        field_valid = False
                        errors.append('too_large')
                else:
                    # The maximum value is not acceptable
                    if not number < max[0]:
                        field_valid = False
                        errors.append('too_large')

            if min[0] is not None:
                if min[1]:
                    # The maximum value is acceptable
                    if not number >= min[0]:
                        field_valid = False
                        errors.append('too_small')
                else:
                    # The maximum value is not acceptable
                    if not number > min[0]:
                        field_valid = False
                        errors.append('too_small')
                
        except:
            field_valid = False
            errors.append('not_a_number')

        # Record the validation results
        valid = valid and field_valid
        fields.append((field_valid, errors))

    return {
        'valid': valid,
        'fields': fields,
    }

def highlight_invalid_field(field, revert: bool=False):
    '''Applies a stylesheet property to an invalid field.
    
    Arguments:
     - field: the field widget object
     - revert: if true, the highlighting is removed
    '''
    print(field)

    #TODO