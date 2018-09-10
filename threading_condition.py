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


def print_nums(condition, is_even):
    """Print numbers."""
    print('call {}'.format('numbers'))
    with condition:
        condition.wait()
        for i in range(101):
            time.sleep(1)
            if is_even and i % 2 == 0:
                print('number {}'.format(i))
            elif not is_even and i % 2 != 0:
                print('number {}'.format(i))


def notifier(condition):
    """Notify other threads."""
    print('call {}'.format('notifier'))
    with condition:
        condition.notifyAll()
        print('notified all')


if __name__ == '__main__':
    condition = threading.Condition()
    th1 = threading.Thread(
        name='Thread_1',
        target=print_nums,
        args=(condition, True)
    )
    th2 = threading.Thread(
        name='Thread_2',
        target=print_nums,
        args=(condition, False)
    )
    th3 = threading.Thread(
        name='Thread_3',
        target=notifier,
        args=(condition,)
    )
    threads = (th1, th2, th3)

    for th in threads:
        th.start()
        time.sleep(1)
