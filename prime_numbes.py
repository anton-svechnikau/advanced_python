"""
HW -- 5.

Output sum of prime numbers in the specified range [n, m).
Use concurrent.futures or/and asyncio.
"""

import asyncio


async def sum_prime_numbers(left_border, right_border):
    """Asynchronously summarize prime numbers."""
    prime_sum = 0
    if left_border <= 0 or right_border <= 0:
        print('Please input positive numbers.')
    elif left_border >= right_border:
        print('The first number should be less than the second.')
    else:
        for prime_number in range(left_border, right_border + 1):
            if prime_number == 1:
                continue

            is_prime = await check_prime_number(prime_number)
            if is_prime:
                print(prime_number)
                prime_sum += prime_number

        print('Sum is {}.'.format(prime_sum))


async def check_prime_number(prime_number):
    """Check if number is prime."""
    is_prime = True
    for num in range(2, int(prime_number ** 0.5) + 1):
        if prime_number % num == 0:
            is_prime = False
            break
    return is_prime


if __name__ == '__main__':
    print('Calculate sum of prime numbers')
    first_num = int(float(input('First number: ')))
    second_num = int(float(input('Second number: ')))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(sum_prime_numbers(first_num, second_num))
    loop.close()
