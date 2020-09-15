def fibo(n) :
    a = 0
    b = 1
    c = 1
    for i in range(n-1) :
        c = a + b
        a = b
        b = c
    return c
n = int(input())
sol = 0
if n != 0 :
    sol = fibo(n)

print(sol)
