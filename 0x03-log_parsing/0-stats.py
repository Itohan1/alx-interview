#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import signal


i = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0}
total_size = 0


def print_code():
    """Prints the status code"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handle(signum, frame):
    """Handles the error signal"""
    print_code()
    sys.exit(0)


signal.signal(signal.SIGINT, handle)

try:
    for line in sys.stdin:
        i += 1
        line = line.split()
        if len(line) < 7:
            continue
        try:
            status_code = int(line[-2])
            file_size = int(line[-1])
        except (ValueError, IndexError):
            continue

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        if i % 10 == 0:
            print_code()

except KeyboardInterrupt:
    sys.exit(0)
