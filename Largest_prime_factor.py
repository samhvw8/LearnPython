import math
import itertools


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for number in itertools.islice(itertools.count(3), int(math.sqrt(n)-1)):
        if n % number == 0:
            return False
    return True


def find_max_prime(n):
    if n <= 3:
        return n
    max = 0
    for i in range(n, 1, -1):
        if is_prime(i) and n % i == 0:
            max = i
        if max != 0:
            return max


def main():
    num = input()

    for i in range(num):
        print find_max_prime(input())


if __name__ == '__main__':
    main()
