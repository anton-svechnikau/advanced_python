"""
HW -- 12.

Comparison of the C ext vs cython vs pure python.
"""

import time
import fib_pure
import fib
import cy_ext.fib_cpy as fib_cpy


strart_time_1 = time.time()
f1 = list(fib_pure.fib(500))
finish_time_1 = time.time() - strart_time_1
print('Pure python  = {}'.format(finish_time_1))

strart_time_2 = time.time()
fib.fib(500)
finish_time_2 = time.time() - strart_time_2
print('C ext python  = {}'.format(finish_time_2))

strart_time_3 = time.time()
fib_cpy.fib(500)
finish_time_3 = time.time() - strart_time_3
print('Cython  = {}'.format(finish_time_3))
