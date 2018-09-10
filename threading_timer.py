"""HW -- 3.

Advance python EPAM courses
Task: Write 5 scripts for each synchronization object:
        - Lock
        - Condition
        - Semaphore
        - Event
        - Timer

"""

import threading
import time


def print_even_nums():
    """Print even numbers."""
    for i in range(0, 101, 2):
        time.sleep(0.1)
        print('number {}'.format(i))


def print_odd_nums():
    """Print odd numbers."""
    for i in range(1, 101, 2):
        time.sleep(0.1)
        print('number {}'.format(i))


if __name__ == '__main__':
    t_1 = threading.Timer(1, print_even_nums)
    t_2 = threading.Timer(1, print_odd_nums)
    t_1.start()
    t_2.start()
