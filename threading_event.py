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


def print_even_nums(event_1, event_2):
    """Print even numbers."""
    print(print_even_nums.__name__)
    for i in range(0, 101, 2):
        event_2.wait()
        event_2.clear()
        print('number {}'.format(i))
        event_1.set()


def print_odd_nums(event_1, event_2):
    """Print odd numbers."""
    print(print_odd_nums.__name__)
    for i in range(1, 101, 2):
        event_1.wait()
        event_1.clear()
        print('number {}'.format(i))
        event_2.set()


if __name__ == '__main__':
    event_1 = threading.Event()
    event_2 = threading.Event()

    th_1 = threading.Thread(target=print_even_nums, args=(event_1, event_2))
    th_2 = threading.Thread(target=print_odd_nums, args=(event_1, event_2))

    event_2.set()
    th_1.start()
    time.sleep(1)
    th_2.start()
