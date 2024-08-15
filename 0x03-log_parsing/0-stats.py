#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import random


i = 0
status_code = []
total_size = 0

for line in sys.stdin:
    line = line.strip()
    string_line = str(line)
    split_it = int(string_line.split(" ")[-2])
    file_size = int(string_line.split(" ")[-1])
    total_size += file_size
    if split_it not in status_code:
        status_code.append(split_it)
        sort_it = sorted(status_code)
    if i % 10 == 0 or KeyboardInterrupt:
        print(f"File size: {total_size}")
    for i in sort_it:
        d_random = random.randint(1, 6)
        print(f"{i}: {d_random}")
        if i == 500:
            print(f"File size: {total_size}") 
i += 1
