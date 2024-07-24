n=str(input())
str="0123456789"
sum=0
for i in n:
    if(i in str):
        sum+=int(i)
print(sum)