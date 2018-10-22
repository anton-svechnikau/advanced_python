"""
HW -- 12.

Pure python implementation of fibonacci.
"""


def fib(n):
    """Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
