# https://www.hackerrank.com/contests/projecteuler/challenges/euler002
def sum_even_fib(n):
    a , b = 0 , 1
    sum_even = 0

    while (b<n):
        if b%2 ==0:
            sum_even+=b
        a , b = b , b + a     
    print sum_even


def main():
    case = input()
    for i in xrange(case):
        n = input()
        sum_even_fib(n)
main()