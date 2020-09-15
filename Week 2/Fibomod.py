def getmod(n, m):
    if n <= 1:
        return n
    a = pisanop(getfibo(m))
    prev = 0
    curr  = 1
    g = n%a
    if g <= 1:
        return g

    for i in range(g-1):
        prev, curr = curr, prev + curr
        if i % 10 == 0:
            prev, curr =  prev , curr
    return curr %m

def pisanop(a):
    p = 0
    ind=0
    c = 0
    b = 1
    for i in range(1,len(a)):
        if((a[i]==0) & (a[i+1]==1)):
            break
    ind = i
    return ind

def getfibo(m):
    x = m*m+1
    a = list()
    a0=0
    a1=1
    a.append(a0)
    a.append(a1)
    for i in range(x):
        a0,a1 = a1,(a0+a1)%m
        a.append(a1)
    return(a)

    
n = input()
b = n.split()
n = int(b[0])
m = int(b[1])
print(getmod(n, m))
