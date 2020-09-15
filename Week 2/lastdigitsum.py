def fibo(n) :
    a = 0
    b = 1
    #print(range(n-1))
    for i in range(n) :
        #print("range", i)
        c = a + b
        a = b
        b = c
        #print(c)

    return c
n = int(input())
sol = 0
if n > 1 :
    sol = fibo(n)
elif n == 1 :
    sol = 1
sol = str(sol)
print(sol[-1])
