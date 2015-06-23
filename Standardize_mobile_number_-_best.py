N = int(input())
A = []
for i in range(N):
    a = raw_input()
    l = len(a)
    A.append(a[l-10:])
A.sort()
for j in A:
    print "+91", j[:5], j[5:]