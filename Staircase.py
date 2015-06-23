# https://www.hackerrank.com/challenges/staircase
DEFAULT = "#"


def draw(o, n, s):
    s += DEFAULT
    print s.rjust(o)
    if n > 1:
        draw(o, n-1, s)


def main():
    num = input()
    draw(num, num, "")


if __name__ == '__main__':
    main()
