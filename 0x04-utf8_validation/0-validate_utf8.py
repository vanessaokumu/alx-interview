#!/usr/bin/python3

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers where each integer represents a byte of data.
    
    Returns:
        bool: True if the data represents a valid UTF-8 encoding, False otherwise.
    """
    # Check for each byte in the data
    num_bytes = 0

    for byte in data:
        # Ensure the byte is between 0 and 255
        if byte < 0 or byte > 255:
            return False
        
        # If we're at the beginning of a character sequence
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character (0xxxxxxx)
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False  # Invalid starting byte for UTF-8
        else:
            # Continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If we've finished processing and still have bytes left to process, it's invalid
    return num_bytes == 0
