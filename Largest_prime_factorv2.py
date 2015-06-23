def find_max_prime(n):
    i = 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def main():
    num = input()

    for i in range(num):
        print find_max_prime(input())


if __name__ == '__main__':
    main()
