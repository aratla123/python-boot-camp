#reverse the  the numbers in a string

inp=str(input())
str1=str(input())
a=(int(str1)) 
print(a) 
sum=0
while(a>0):
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(sum)


