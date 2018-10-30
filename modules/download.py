import os

from defusedxml import ElementTree
from xml.etree.ElementTree import Element
from urllib import request

from .podcast import Episode
from .string import str_to_filename, command_line_to_bool
from .xml import get_unique_xml_element

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
