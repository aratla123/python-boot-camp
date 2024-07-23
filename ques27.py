# sum of squares of even and odd digits of a number

n=int(input())
even=0
odd=0
while(n>0):
    d=n%10
    if(d%2==0):
        even+=(d)**2
    else:
        odd+=(d)**2
    n=n//10
print(even)
print(odd)