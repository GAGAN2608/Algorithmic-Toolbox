# Uses python3
import sys

def get_change(n):
    #write your code here
    #print("hi",n)
    c=0
    while n>0 :
        if n == 0:
            break
        if n > 10 :
            c=c+1
            n=n-10
        elif n>=5 and n<=9:
            c=c+1
            n=n-5
        else:
    #        print("hi")
            c=c+n
            n=n-n
    #print(n,c)
    return c

n = int(input())
print(get_change(n))
