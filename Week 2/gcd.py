def gcd(a, b) :
    g = 1
    while b != 0 :
        g = a % b
        a = b
        b = g
    return a

n = input()
b = n.split()
ans = 1
#print(type(ans))
#print(type(b[0]))
b[0] = int(b[0])
b[1] = int(b[1])
#print(type(b[0]))
if(b[0] > b[1]) :
    ans = gcd(b[0], b[1])
else :
    ans = gcd(b[1], b[0])

#print(type(ans))
print(ans)
