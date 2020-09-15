def fibo(m) :
    listt = list()
    listt.append(0)
    listt.append(1)
    for i in range(2, m+1) :
        listt.append((listt[i-1] + listt[i-2])%10)
    return listt
a = input()
b = a.split()
n = int(b[0])
m = int(b[1])
m = m % 60
listt = list()
ans = 0
if m >= 2 :
    listt = fibo(m)
    for i in range(n, m+1) :
        ans+= listt[i]
elif m == 1 and n == 1 or n == 0 and m == 1:
    ans = 1
#print(listt)
#nfibo = listt[n-2]
#mfibo = listt[m]
#print(mfibo)
#print(nfibo)
ans = str(ans)
print(ans[-1])
