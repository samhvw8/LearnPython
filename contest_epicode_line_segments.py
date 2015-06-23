class pairc(object):
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
    def __ge__(self, other):
        return self.a <= other.a and self.b >= other.b
    def __le__(self, other):
        return self.a >= other.a and self.b <= other.b
    def __str__(self):
        ret = "("
        ret += str(self.a) + "," + str(self.b) + ")"
        return ret
    def __len__(self):
        return self.b-self.a

def check_condtion(sset, l, i):
    for j in xrange(len(l)):
        if i != j:
            if l[j] <= sset :
                return False
    return True


test_c = input()
l = []
for i in range(test_c):
    pair = map(int,list(raw_input().split()))
    pair = pairc(pair[0],pair[1])
    l.append(pair)
s = dict()
for i in xrange(len(l)):
    if check_condtion(l[i], l, i):
        if len(l[i]) in s:
            s[len(l[i])] += 1
        else:
            s[len(l[i])] = 1
        print l[i], len(l[i])
