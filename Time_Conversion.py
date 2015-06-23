# https://www.hackerrank.com/challenges/time-conversion


def main():
    time = raw_input().split(':')
    att = time[2][2:]
    time[2] = time[2][:2]

    if att == 'AM':
        if (int(time[0] == '12')):
            print "00" + ":" + time[1] + ":" + time[2]
        else:
            print time[0] + ":" + time[1] + ":" + time[2]
    if att == 'PM':
        if (int(time[0] == '12')):
             print time[0] + ":" + time[1] + ":" + time[2]
        else:
            print str(int(time[0]) + 12) + ":" + time[1] + ":" + time[2]


if __name__ == '__main__':
    main()
