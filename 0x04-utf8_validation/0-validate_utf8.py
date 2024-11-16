#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): A list of integers where each integer represents 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Get the least significant 8 bits of the integer
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check that the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
        num_bytes -= 1

    return num_bytes == 0
