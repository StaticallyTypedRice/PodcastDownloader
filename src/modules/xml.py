from defusedxml import ElementTree
from urllib import request

from xml.etree.ElementTree import Element

class XmlElementNotFound(Exception):
    '''The exception that is raised when an XML element was not found.'''

class XmlElementNotUnique(Exception):
    '''The exception that is raised when an XML element is not unique.'''

def get_unique_xml_element(scope: Element, element: str) -> Element:
    '''Returns an XML element if it is unique in the current scope.
    Returns an error if it is not unique or was not found.

    Uses defusedxml for parsing.

    Arguments:
        scope: The current XML scope.
        element: The name of the element.

    '''

    # Find all occurances of the specified element
    elements = scope.findall(element)

    if len(elements) == 0:
        # If there are no elements, raise an error.
        raise XmlElementNotFound(f'Could not find the <{element}> element.')
    elif len(elements) > 1:
        # If there is more than one element, raise an error.
        raise XmlElementNotUnique(f'There is more than one <{element}> element.')
    else:
        # Return the element
        return elements[0]

def parse_remote_xml(url: str) -> Element:
    '''Parse a remote XML file using defusedxml.

    Arguments:
        url: The URL of the XML file.
    '''

    # Request the XML file
    xml_string = request.urlopen(url).read()

    # Return the parsed the XML file
    return ElementTree.fromstring(xml_string)
    