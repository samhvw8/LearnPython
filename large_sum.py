def check(num_list):
    for num in num_list:
        if num != []:
            return 0
    return 1


no_number = input()

list_num = raw_input().split()
for i in range(len(list_num)):
    list_num[i] = map(int,list(list_num[i]))

sum_ = []
remain = 0
while True:
    plus = 0
    if remain != 0:
        plus += remain
        remain = 0
    if check(list_num):
        sum_.append(plus)
        break

    for num in list_num:
        if num != []:
            plus += num.pop(-1)

    if plus > 9:
        remain += plus/10
        plus %= 10

    sum_.append(plus)

print int(''.join(map(str,sum_[::-1])))


