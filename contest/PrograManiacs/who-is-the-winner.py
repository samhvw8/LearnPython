# https://www.hackerrank.com/contests/programaniacs-june-15/challenges/who-is-the-winner
def who_win(l_string):
    count = dict()
    for char in l_string:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    return count

STRING = list(raw_input())
max_ = sorted(who_win(STRING).items(), key = lambda x: x[1])[::-1];
maxv = max_[0]
for i in max_:
    if i[1] == maxv[1] and i[0] != maxv[1]:
        maxv = i
    if i[1] < maxv[1]:
        break

print maxv[0]
