import sys
DNS_ZONE_FILE = sys.argv[1]



def getKey(item):
    return item[1]


def sortlist(list_ip,data_dict):
    return sorted(list_ip,  key=data_dict.__getitem__)


def getdetail(line):
    detail = line.split()
    return detail


def main():
    # Check Argv
    if(len(sys.argv) != 2):
        exit("python {} <DNS-ZONE-FILE>".format(argv[0]))

    f = open(DNS_ZONE_FILE, "r")
    fout = open("output.txt","w")

    type_dict = dict()
    data_dict = dict()
    header = ""
    for line in f:
        if line[0] == ';':
            continue
        if line[0] == '\n':
            continue
        if line[0] != ' ':
            detail_line = getdetail(line)
            if detail_line[0] == '$TTL':
                for sub_line in f:
                    if sub_line == ';\n':
                        break
                    line += sub_line
                header += line
                continue
                
            if detail_line[0] != '$TTL':
                if len(detail_line) > 3:
                    if detail_line[2].isalpha():
                        # import type to dict
                        if detail_line[2] not in type_dict:
                            type_dict[detail_line[2]] = []
                        type_dict[detail_line[2]].append(detail_line[3])
                    else:
                        # import type to dict
                        if detail_line[1] not in type_dict:
                            type_dict[detail_line[1]] = []
                        type_dict[detail_line[1]].append(detail_line[3])
                    # import data to dict
                    data_dict[detail_line[3]] = detail_line
                elif len(detail_line) == 3:
                    # import type to dict
                    if detail_line[1] not in type_dict:
                        type_dict[detail_line[1]] = []
                    type_dict[detail_line[1]].append(detail_line[2])
                    data_dict[detail_line[2]] = detail_line
    

    for key in type_dict:
        type_dict[key] = sortlist(type_dict[key],data_dict)

    print(header)
    for key in type_dict:
        list_ip = type_dict[key]
        print("\n;\n")
        print("; {}\n".format(key))
        print(";\n\n")
        for ip in list_ip:
            print(data_dict[ip])
    fout.close()
    f.close()


if __name__ == '__main__':
    main()
