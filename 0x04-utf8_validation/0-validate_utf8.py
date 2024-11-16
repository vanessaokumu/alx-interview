#!/usr/bin/python3

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers where each integer represents a byte of data.
    
    Returns:
        bool: True if the data represents a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes to be checked in a multi-byte sequence
    num_bytes = 0

    for byte in data:
        # Check for the number of leading 1's in the byte
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid starting byte for UTF-8
        else:
            # Check if it is a continuation byte (should start with 10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    
    # If we finish and there's still a byte expected, the data is invalid
    return num_bytes == 0
