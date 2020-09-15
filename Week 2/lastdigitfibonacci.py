def fibo(n) :
    a = 0
    b = 1
    for i in range(n-1) :
        c = a + b
        c = c % 10
        a = b
        b = c
    return b
n = int(input())
sol = 1
if n > 2 :
    sol = fibo(n)
sol = str(sol)
print(sol[-1])
