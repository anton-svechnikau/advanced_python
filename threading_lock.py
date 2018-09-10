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

LOCK = threading.Lock()


class NewThread(threading.Thread):
    """New thread class."""

    def __init__(self, name, delay, is_even):
        """Init method."""
        threading.Thread.__init__(self)
        self.name = name
        self.is_even = is_even
        self.delay = delay

    def run(self):
        """Standard method of Thread class."""
        print('starting {}'.format(self.name))
        LOCK.acquire()
        print_num(self, self.is_even, self.delay)
        LOCK.release()


def print_num(thread, even, delay):
    """Print numbers."""
    for i in range(101):
    time.sleep(delay)
    if even and i % 2 == 0:
            print('{}: {}'.format(thread.name, i))
    elif not even and i % 2 != 0:
        print('{}: {}'.format(thread.name, i))


if __name__ == '__main__':
    t1 = NewThread('thread_1', 1, True)
    t2 = NewThread('thread_2', 1, False)

    threads = (t1, t2)

    for t in threads:
        t.start()

    for t in threads:
        print('j')
        t.join()

    print('main thread')
