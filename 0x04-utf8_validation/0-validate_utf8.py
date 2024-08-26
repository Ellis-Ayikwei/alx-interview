#!/usr/bin/python3
"""
Defines a method that determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate UTF-8 encoding in a given binary data.
    """
    i = 0
    while i < len(data):
        byte = data[i]
        if byte < 0x80:  # 0xxxxxxx: 1 byte
            i += 1
        elif byte < 0xC0:  # 110xxxxx: 2 bytes
            return False
        elif byte < 0xE0:  # 1110xxxx: 3 bytes
            if i + 1 >= len(data) or data[i+1] < 0x80 or data[i+1] >= 0xC0:
                return False
            i += 2
        elif byte < 0xF0:  # 11110xxx: 4 bytes
            if i + 2 >= len(data) or data[i+1] < 0x80 or data[i+1] >= 0xC0 or \
                    data[i+2] < 0x80 or data[i+2] >= 0xC0:
                return False
            i += 3
        else:
            return False
    return True
