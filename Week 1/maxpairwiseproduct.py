n = int(input())
pro = 1
ans = 0
i = 0
j = input()
listt = list()
listt = j.split()
for i in range(n) :
    listt[i] = int(listt[i])
#print(listt)
listt.sort()
#for j in range(int(n)) :
#    for h in range(int(j + 1), int(n)) :
#        pro = int(listt[j]) * int(listt[h])
#        if pro > ans :
#            ans = pro

#i = i + 1
a = max(listt)
listt.remove(a)
b = max(listt)
#print(listt)
print(int(a)*int(b))
