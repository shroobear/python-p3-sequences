#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    if length > 0:
        fibonacci_list.append(0)
    if length > 1:
        fibonacci_list.append(1)
    for n in range(2, length):
        acc = (fibonacci_list[-1] + fibonacci_list[-2])
        fibonacci_list.append(acc)
    print(fibonacci_list)