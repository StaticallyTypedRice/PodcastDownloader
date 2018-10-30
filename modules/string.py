def str_to_filename(name: str, placeholder: str='') -> str:
    '''A rudimentary function for parsing a string into a valid file name.
    
    Removes invalid file name characters.

    NOTE: There is no guarantee that the string returned is will always be a valid 
          file name, but it should be valid in most cases.

    Arguments:
        name: The string to be parsed.
        placeholder: Replace invalid file name characters with this string.
    '''

    invalid_characters = [
        '\\',
        '/',
        ':',
        '*',
        '?',
        '"',
        '<',
        '>',
        '|',
    ]

    for character in invalid_characters:
        name = name.replace(character, placeholder)

    return name

def command_line_to_bool(string: str, strict=True) -> bool:
    '''Parses the strings 'y', 'yes', 'n' or 'no' to a boolean.

    The strings are not case sensitive.

    Arguments:

        string: The string to be parsed.

        strict: If True, only 'y', 'yes', 'n' and 'no' will be parsed, 
                with other strings raising a ValueError.
                If False, 'y' and 'yes' will return True and other strings
                will return False. 
    
    NOTE: This is different from using the bool() function on a string.
          The bool() function returns false for an empty string,
          and returns true otherwise. This function parses the words
          'y', 'yes', 'n' and 'no' into a boolean.'''

    # Use the lower-case version of the string
    string_lowercase = string.lower()

    if string_lowercase == 'y' or string_lowercase == 'yes':
        # the string is equal to 'y' or 'yes'
        return True
    else:
        if strict:
            if string_lowercase == 'n' or string_lowercase == 'no':
                # the string is equal to 'n' or 'no'
                return False
            else:
                # The string is invalid
                raise ValueError(
                    f'The string \'{string}\' is invalid. '
                    'Only \'y\', \'yes\', \'n\' or \'no\' are valid in strict mode.'
                )
        else:
            # The string does not equal 'y' or 'yes'
            return False
