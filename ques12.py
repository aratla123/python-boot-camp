# code for min element in a list

lst=list(map(int,input().split()))
b=0
for i in range(0,len(lst)):
    if(lst[i]<b):
        b=lst[i]
print(b)        