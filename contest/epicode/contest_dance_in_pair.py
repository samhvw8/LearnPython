class nodet:
    "BST node"
    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data
        self.count = 1
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = nodet(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = nodet(data)
            else:
                self.right.insert(data)
        elif data == self.data:
            self.count += 1
    def search(self, data):
        if self == None:
            print "Self is node"
            return 0
        elif self.data == data and self.count > 0:
            return 1
            self.count -= 1
        elif data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return 0
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return 0

def count(MALE, rfemale, k):
    count = 0
    j = 0
    while len(MALE) != 0 and j <= k:
        for i in range(len(MALE)):
            if rfemale.search(MALE[i] + j):
                count += 1
                MALE.pop(i)
                break
        j += 1
    return count

def main():
    INFO = map(int,raw_input().split())
    MALE = map(int,raw_input().split())
    FEMALE = map(int,raw_input().split())
    MALE = sorted(MALE)
    rfemale = nodet(FEMALE[0])
    for i in xrange(1,len(FEMALE)):
        rfemale.insert(FEMALE[i])
    print count(MALE, rfemale, INFO[1])

if __name__ == '__main__':
    main()
