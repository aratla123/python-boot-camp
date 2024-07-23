n=int(input())
r=n**0.5
count=0
if(n==1):
 print("not a prime number")
else:
 print("prime number")
for i in range(2,int(r+1)):
 if(n%i==0):
  count=1
  break
 if(count==0):
  print("not a prime number")
else:
  print("prime number")
 