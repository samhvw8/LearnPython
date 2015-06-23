import commands


def change_name():
    file_name = commands.getoutput(
        'ls /home/ginz/Documents/Python'
    )
    file_name = file_name.split('\n')
    new_file_name = file_name[:]

    for i in range(len(new_file_name)):
        new_file_name[i] = new_file_name[i].replace(' ','_')

    for i in xrange(len(new_file_name)):
        result = commands.getoutput(
            'mv "{}" {}'.format(file_name[i],new_file_name[i])
        )
        print result


def main():
    change_name()

if __name__ == '__main__':
    main()
