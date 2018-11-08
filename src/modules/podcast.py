from xml.etree.ElementTree import Element

from modules.xml import get_unique_xml_element

class Episode(object):
    '''The podcast episode object.'''

    def __init__(self, item: Element):
        '''Create an Episode object from an RSS item.
        
        An example RSS file:
            <rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
                <channel>

                    <!-- RSS metadata -->

                    <item>
                        <guid>1234</guid>
                        <title>Episode Title</title>
                        <description>Episode Description</description>
                        <pubDate>Date Published</pubDate>
                        <enclosure url="https://example.com/episode.mp3" type="audio/mpeg" />
                    </item>

                    <!-- ... -->

                </channel>
            </rss>

        Arguments:
            element: The <item> element for the episode.
        '''

        # Parse the RSS item
        self.guid = get_unique_xml_element(item, 'guid').text
        self.title = get_unique_xml_element(item, 'title').text
        self.date = get_unique_xml_element(item, 'pubDate').text
        self.url = get_unique_xml_element(item, 'enclosure').get('url')

        # The file name is the final item in the URL path
        self.file_name = self.url.split('/')[-1]

        # The file extension is the final item in the file name
        self.file_extension = self.file_name.split('.')[-1]
