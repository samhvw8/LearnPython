def insertion_sort(list_num):
    for index in range(1,len(list_num)):

        current_value = list_num[index]
        pos = index

        while pos > 0 and current_value < list_num[pos-1]:
            list_num[pos] = list_num[pos-1]
            pos = pos - 1

        list_num[pos] = current_value
        for val in list_num:
            print val ,
        print


no = input()

list_num = map(int,raw_input().split())

insertion_sort(list_num)
