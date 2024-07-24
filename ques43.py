# sum of digits using ascii values

n=str(input())
str="0123456789"
sum=0
for i in n:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print((sum))