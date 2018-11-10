import tkinter as tk

from defusedxml import ElementTree

from modules.xml import get_unique_xml_element, parse_remote_xml
from modules.download import podcast_download

def startup():
    '''The startup GUI function.'''
    
    # Create the TkInter window
    window = tk.Tk()

    window.title("Podcast Downloader")

    # Start the GUI
    window.mainloop()

if __name__ == '__main__':
    startup()
