n=int(input())
sum=0
b=n
while(b>0):
   rem=b%10
   b=b//10
   sum=sum+rem*rem*rem
if(sum==n):
    print("numnber is armstrong")
else:
    print("number is not armstrong")