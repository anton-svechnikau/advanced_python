"""HW -- 2.

Advance python EPAM courses
Task: Write script which causes segmentation fault error

"""

import ctypes
import sys


def crash_using_recursion():
    """Implementation of segfault by recursion."""
    print('Recursion method.')
    sys.setrecursionlimit(sys.getrecirsionlimit << 10)

    def f(f):
        f(f)

    f(f)


def crash_using_ctypes():
    """Implementation of segfault by ctypes."""
    print('Ctypes method.')
    address = 0
    string = ctypes.string_at(address)
    return string


def main():
    """Main func."""
    print(('Hello! Please choose method to cause segmentation fault error in '
           'python 3.6.5:\n1 -- Crash using recursion limits;\n2 -- Crash '
           'using ctypes.'))
    choice = input('Your choice (1 or 2): ')

    if choice == '1':
        crash_using_recursion()
    elif choice == '2':
        crash_using_ctypes()
    else:
        print('Invalid choice')


if __name__ == "__main__":
    main()
