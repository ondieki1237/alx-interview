#!/usr/bin/python3
import sys
import signal

# Initialize total file size and status code dictionary
total_size = 0
status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

def print_stats():
    """ Print the total size and status code counts in ascending order """
    print("File size:", total_size)
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def handle_interrupt(signum, frame):
    """ Signal handler for keyboard interrupt (CTRL + C) """
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        if len(parts) < 7:
            continue  # Skip lines that do not have enough parts
        
        # Extract file size and status code
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue  # Skip lines with invalid file size or status code

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle interrupt to print the final stats
    print_stats()
    raise
