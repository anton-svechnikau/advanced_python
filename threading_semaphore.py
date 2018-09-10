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


def print_even_nums(even_semaphore, odd_semaphore):
    """Print even numbers."""
    print(print_even_nums.__name__)
    for i in range(0, 101, 2):
        even_semaphore.acquire()
        print('number {}'.format(i))
        odd_semaphore.release()


def print_odd_nums(even_semaphore, odd_semaphore):
    """Print odd numbers."""
    print(print_odd_nums.__name__)
    for i in range(1, 101, 2):
        odd_semaphore.acquire()
        print('number {}'.format(i))
        even_semaphore.release()


if __name__ == '__main__':
    sem_1 = threading.Semaphore(1)
    sem_2 = threading.Semaphore(0)

    th_1 = threading.Thread(target=print_even_nums, args=(sem_1, sem_2))
    th_2 = threading.Thread(target=print_odd_nums, args=(sem_1, sem_2))

    th_1.start()
    time.sleep(1)
    th_2.start()
