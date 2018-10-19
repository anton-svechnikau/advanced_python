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
    for i in range(101):
        condition.acquire()
        condition.notify_all()
        time.sleep(0.5)
        if is_even and not i % 2:
            print('number {}'.format(i))
            condition.wait()
        elif not is_even and i % 2:
            print('number {}'.format(i))
            condition.wait()
        condition.release()


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

    th1.start()
    th2.start()

    # th1.join()
    th2.join()
