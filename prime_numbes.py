
def prime_numbers(number):
    sums = 0
    if number <= 0:
        print('input positive number')

    for prime_number in range(number + 1):
        if prime_number == 1:
            continue

        is_prime = True
        for num in range(2, int(prime_number ** 0.5) + 1):
            if prime_number % num == 0:
                is_prime = False
                break

        if is_prime:
            sums += prime_number
            print(prime_number)

    print('Sum is {}'.format(sums))

if __name__ == '__main__':
    print('Print positive number to calculate sum of prime numbers')
    num = input('Your number: ')
    prime_numbers(int(num))
