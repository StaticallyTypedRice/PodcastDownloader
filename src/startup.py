import sys

from defusedxml import ElementTree

from modules.xml import get_unique_xml_element, parse_remote_xml
from modules.download import podcast_download
from modules.gui import *

def startup():
    '''The startup GUI function.'''

    # Start the GUI
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    startup()
