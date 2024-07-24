'''inp=str(input())
for i in inp:
    if(ord(i)>=60 and ord(i)<=90):#print(chr(ord(i)+4))
       n=ord(i)
    print(chr(n+4))'''  

n=input()
for i in n:
    n=ord(i)+4
    if n<=122:
        print(chr(n),end="")
    else:
        print(chr(n-26),end=" ")