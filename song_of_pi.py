# https://www.hackerrank.com/challenges/song-of-pi
def check_pi_song(string, py):
    for i in range(len(string)):
        if len(string[i]) != py[i]:
            return 0
    return 1


py = "31415926535897932384626433833"
py = map(int, list(py))
case = input()
for i in range(case):
    string = raw_input().split()
    if check_pi_song(string, py):
        print "It's a pi song."
    else:
        print "It's not a pi song."
