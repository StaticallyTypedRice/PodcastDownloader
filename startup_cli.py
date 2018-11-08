from defusedxml import ElementTree

from modules.xml import get_unique_xml_element, parse_remote_xml
from modules.download import podcast_download
from modules.string import command_line_to_bool

def startup():
    '''The startup function.'''

    print()
    print(' ############### Podcast Downloader ###############')
    print(' #                                                #')
    print(' # Created by Richie Zhang                        #')
    print(' # Version 0.1                                    #')
    print(' #                                                #')
    print(' # Downloads all podcasts in an RSS file.         #')
    print(' #                                                #')
    print(' ##################################################')
    print()

    # Ask if the RSS file is remote or local
    remote_rss_input = None
    while remote_rss_input is None:
        remote_rss_input = input('Is the RSS file remote or local?\n1: Remote (default)\t2: Local\n')
        if not remote_rss_input or remote_rss_input == '1':
            remote_rss = True
        elif remote_rss_input == '2':
            remote_rss = False
        else:
            remote_rss_input = None

    # Ask for the RSS file
    rss_source = ''
    while not rss_source:
        rss_source = input(f'The RSS {"URL" if remote_rss else "path"}: ')
    
        try:
            # Parse the RSS file
            if remote_rss:
                rss = parse_remote_xml(rss_source)
            else:
                rss = ElementTree.parse(rss_source)
        except Exception as e:
            # If there is an error, print it and ask for the RSS file again
            print(str(e))
            rss_source = ''

    # Ask for the delay time
    delay_input = None
    while delay_input is None:
        try:
            delay_input = input('The delay time between downloads (1 second): ')
            if delay_input:
                delay = int(delay_input)
            else:
                delay = 1
        except Exception as e:
            print(str(e))
            delay_input = None

    # Ask for the output directory
    output_dir = input('The output directory (download): ')
    if not output_dir:
        output_dir = 'download'
    
    # Ask whether to rename the downloaded files
    rename_input = None
    while rename_input is None:
        rename_input = input('Use the episode name for the file name? (yes): ')
        if rename_input:
            try:
                rename = command_line_to_bool(rename_input, strict=True)
            except ValueError:
                rename_input = None
        else:
            rename = True

    print('Starting download...\n')

    # Count the total number of files
    total_files = len(rss.findall('channel/item'))
    print(f'{str(total_files)} file{"s" if total_files != 1 else ""} in total.\n')

    # Call the download function
    download = podcast_download(rss, delay, output_dir, rename, print_progress=True)

    print('Download complete\n')
    print(f'{str(download["total_downloads"])} files downloaded.')
    print(f'{str(download["total_errors"])} errors.')

    # Prevent the window from closing when the download is complete
    input('\nPress ENTER to exit')

if __name__ == '__main__':
    startup()
