import os

from defusedxml import ElementTree
from xml.etree.ElementTree import Element
from urllib import request

from modules.podcast import Episode
from modules.string import str_to_filename, command_line_to_bool
from modules.xml import get_unique_xml_element, parse_remote_xml

def podcast_download(rss: Element, delay: int=0, output_dir: str='',
                     rename: bool=False, print_progress: bool=False) -> dict:
    '''The main function.

    Download all episodes in a podcast.

    Arguments:
        url: The podcast RSS.
        delay: The delay in seconds between file downloads.
        output_dir: The output directory name (or the same directory if an empty string is supplied).
        rename: Whether to rename the downloaded file to the name of the to the episode.
        print_progress: Whether to print the download progress to the console.
    '''

    # Count the number of files downloaded and the number of errors
    files_downloaded = 0
    file_errors = 0

    # Keep a record of the download progress
    download_progress = []

    # Set the download path
    # os.path.join() returns a path ending in a slash when a second argument is an empty string,
    # and a path not ending in a slash otherwise.
    if output_dir:
        output_dir = os.path.join(os.getcwd(), output_dir)

        # If the output directory does not exist, create it
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
    else:
        output_dir = os.getcwd()
    

    # Find all RSS <item> elements
    items = rss.findall('channel/item')
    
    for item in items:

        # Parse the <item> element for the episode
        episode = Episode(item)

        if print_progress:
            print(f'Downloading "{episode.title}"')
             
        if rename:
            # Rename the file to the episode title
            filename = f'{str_to_filename(episode.title)}.{str_to_filename(episode.file_extension)}'
        else:
            # Keep the file name as is
            filename = str_to_filename(episode.file_name)

        filepath = os.path.join(output_dir, filename)

        try:
            request.urlretrieve(episode.url, filepath)

            files_downloaded += 1
            download_progress.append({
                'file': filename,
                'downloaded': True,
            })
        except Exception as e:
            if print_progress:
                print(f'  ERROR -> {str(e)}')

            file_errors += 1
            download_progress.append({
                'file': filename,
                'downloaded': False,
                'error': str(e),
            })

    # Return data about the download process
    return {
        'total_items': len(items),
        'total_downloads': files_downloaded,
        'total_errors': file_errors,
        'downloads': download_progress,
    }

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

    # Call the download function
    download = podcast_download(rss, delay, output_dir, rename, print_progress=True)

    print('Download complete\n')
    print(f'{str(download["total_downloads"])} files downloaded.')
    print(f'{str(download["total_errors"])} errors.')

    # Prevent the window from closing when the download is commplete
    input('\nPress ENTER to exit')

if __name__ == '__main__':
    startup()
