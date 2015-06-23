#https://www.hackerrank.com/challenges/taum-and-bday

def check(b,w,ex):
    if b == w:
        return 0
    elif ex > b and ex > w:
        return 0
    elif ex < b and ex >= w:
        if w+ex > b:
            return 0
        return 2
    elif ex < w and ex >= b:
        if b+ex > w:
            return 0
        return 1
    elif ex < w and ex < b:
        disw = w - ex
        disb = b - ex
        if disw < disb:
            if w+ex > b:
                return 0
            return 2
        else:
            if b+ex > w:
                return 0
            return 1
    pass

def costreduce(numlist,costlist):
    nl = numlist # 2 element
    cl = costlist # 3 element
    cost = 0
    checkc = check(cl[0],cl[1],cl[2])
    if checkc == 1:
        cost += cl[0]*nl[0] # black
        cost += (cl[0]+cl[2])*nl[1] #black --> white
    elif checkc == 2:
        cost += cl[1]*nl[1] # white
        cost += (cl[1]+cl[2])*nl[0] #white -->black
    else:
        cost += cl[0]*nl[0] # black
        cost += cl[1]*nl[1] # white
    return cost


num = input()
for i in range(num):
    numbergift = map(int,raw_input().strip().split())
    costgift = map(int,raw_input().strip().split())
    print costreduce(numbergift,costgift)
