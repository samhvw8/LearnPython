# https://www.hackerrank.com/challenges/cavity-map


def check_condtion(l, row, col, size):
    if row == 0 or col == 0 or row == size - 1 or col == size - 1:
        return False
    val = l[row][col]
    if val <= l[row - 1][col]:
        return False
    if val <= l[row + 1][col]:
        return False
    if val <= l[row][col - 1]:
        return False
    if val <= l[row][col + 1]:
        return False
    return True


def draw(l, cavity):
    for i in cavity:
        l[i[0]][i[1]] = 'X'
    for row in l:
        s = ""
        for num in row:
            s += str(num)
        print s


def main():
    size = input()
    arr = []
    for i in range(size):
        l = list(raw_input())
        # if i < size - 1:
           # l = l[:-1]
        l = map(int, l)
        arr.append(l)

    cavity_list = []

    for i in range(size):
        for j in range(size):
            if check_condtion(arr, i, j, size):
                cavity_list.append((i, j))

    draw(arr, cavity_list)

if __name__ == '__main__':
    main()
