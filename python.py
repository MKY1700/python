a = int(input())
b = 0
c = a
for i in range(a):
    b += 1
    c -= 1
    print(" "*(c),"*"*(b+i))
b = a
c = 0
for i in range(a):
    b -= 1
    c += 1
    print(" "*(c),"*"*(b+b-1))