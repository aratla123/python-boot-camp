#reverse of a number

n=1234
rev=""
temp=0
while(n>0):
 rem=n%10
 rev=rev+str(rem)
 n=n//10
ans=int(rev)
print(ans)
print(type(ans))