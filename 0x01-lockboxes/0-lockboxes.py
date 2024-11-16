#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): A list of lists where each sublist contains the keys for the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]
    
    while keys:
        key = keys.pop()
        if key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])
    
    return all(opened)
