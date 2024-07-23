n=int(input())
rev=0
a=n
while(a>0):
 rem=a%10
 rev=(rev*10)+rem
 a=a//10
if(n==rev):
   print("palindrome")
else:
   print("not a palindrome")