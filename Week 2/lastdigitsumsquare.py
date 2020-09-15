def fibo(m) :
    if m <=1 :
        return m
    listt = list()
    listt.append(0)
    listt.append(1)
    for i in range(2, m+1) :
        listt.append((listt[i-1] + listt[i-2])%10)
    return listt
a = int(input())
a%= 60
listt = list()
ans = 0
if a >=2 :
    listt = fibo(a)
    print(listt)
    for i in range(a+1) :
        ans+= listt[i]**2
elif a == 1 :
    ans = 1
ans = str(ans)
print(ans[-1])
