#!/usr/bin/python3
"""
    This module prints a text with 2 new lines after ., ? and :
    using the method: text_indentation
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    character = ".?:"
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in character:
            print('\n')
            i += 2
        else:
            i += 1
