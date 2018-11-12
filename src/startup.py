from tkinter import *

from defusedxml import ElementTree

from modules.xml import get_unique_xml_element, parse_remote_xml
from modules.download import podcast_download

# Constants
PROGRAM_NAME = 'Podcast Downloader'
PROGRAM_INTRO_TEXT = 'Download all episodes of a podcast.'

def startup():
    '''The startup GUI function.'''
    
    # Create the TkInter root
    root = Tk()

    # Create a frame for the main form
    main_form = Frame(root)

    # Add UI metadata
    root.title(PROGRAM_NAME)

    # This label breaks the UI layout
    #Label(main_form, text=PROGRAM_INTRO_TEXT).grid(row=1, sticky=E)

    # Add the UI elements
    
    Label(main_form, text='Podcast source:').grid(row=1, column=1, padx=5, sticky=E)
    Entry(main_form).grid(row=1, column=2, padx=5, sticky=E)
    
    Label(main_form, text='Podcast location:').grid(row=2, column=1, padx=5, sticky=E)
    Entry(main_form).grid(row=2, column=2, padx=5, sticky=E)

    Label(main_form, text='Delay between downloads:').grid(row=3, column=1, padx=5, sticky=E)
    Entry(main_form).grid(row=3, column=2, padx=5, sticky=E)

    Label(main_form, text='Download to:').grid(row=4, column=1, padx=5, sticky=E)
    Entry(main_form).grid(row=4, column=2, padx=5, sticky=E)

    Label(main_form, text='Rename each file to the episode name?').grid(row=5, column=1, padx=5, sticky=E)
    Entry(main_form).grid(row=5, column=2, padx=5, sticky=E)

    download_button = Button(main_form, text='Download')
    download_button.grid(row=6, column=2, sticky=E)

    # Start the GUI
    main_form.grid()
    root.mainloop()

if __name__ == '__main__':
    startup()
