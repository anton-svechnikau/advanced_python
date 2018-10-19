"""HW -- 4.

Advance python EPAM courses
Task: Output numbers from 0..100 in order.
First process outputs even numbers.
Second process outputs odd numbers.
You can use any synchronization objects.

"""

import time
from multiprocessing import Process, Lock


def print_nums(lock, even, proc_name):
    """Print numbers."""
    for n in range(101):
        time.sleep(.1)
        lock.acquire()
        if even and n % 2 == 0:
            print("Number in {}: {}".format(proc_name, n))
        elif not even and n % 2 != 0:
            print("Number in {}: {}".format(proc_name, n))
        lock.release()


if __name__ == '__main__':
    LOCK = Lock()

    p_1 = Process(target=print_nums, args=(LOCK, True, 'Proc_1'))
    p_2 = Process(target=print_nums, args=(LOCK, False, 'Proc_2'))

    p_1.start()
    p_2.start()
