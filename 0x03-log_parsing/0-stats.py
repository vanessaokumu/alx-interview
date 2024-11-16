#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics.
"""

import sys

def print_stats(total_size, status_counts):
    """
    Prints the computed metrics.
    
    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary with status codes and their counts.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 6:
            status_code = parts[-2]
            file_size = parts[-1]
            try:
                total_size += int(file_size)
                if int(status_code) in status_counts:
                    status_counts[int(status_code)] += 1
            except ValueError:
                pass
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
print_stats(total_size, status_counts)
