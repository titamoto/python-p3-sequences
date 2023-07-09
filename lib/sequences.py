#!/usr/bin/env python3


def print_fibonacci(length):
   if length == 0:
    print([])
   elif length == 1:
    print([0])
   elif length >= 2:
    s = [0, 1]
    i = 2
    while i < (length):
        s.append(s[-1] + s[-2])
        i += 1
    print(s)