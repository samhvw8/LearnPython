# https://www.hackerrank.com/challenges/caesar-cipher-1
def encode(list_s, k):
    ret = list_s[:]
    for i in range(len(ret)):
        if (ret[i] <= 'z' and ret[i] >= 'a'):
            if ord(ret[i]) + k <= ord('z'):
                ret[i] = chr(ord(ret[i]) + k)
            else:
                ret[i] = chr(ord('a') + k - (ord('z') - ord(ret[i]) + 1))
        if (ret[i] <= 'Z' and ret[i] >= 'A'):
            if ord(ret[i]) + k <= ord('Z'):
                ret[i] = chr(ord(ret[i]) + k)
            else:
                ret[i] = chr(ord('A') + k - (ord('Z') - ord(ret[i]) + 1))

    return ''.join(ret)


length = input()
string = list(raw_input())
k = input()
k %= 26
print encode(string, k)
