'''replace the element in an array with  avg of max and min elements
testcase:0
13 2 67 20 68:
explanation: (2+68)//2=34  [13 2 67 20 68]=[34 34 34 34]'''

lst=list(map(int,input().split()))
max=0
min=0

for i in range(0,len(lst)):
    if(lst[i]>max):
        max=lst[i]
    
    if(lst[i]<min):
         min=lst[i]
         
print(max)
print(min)
for i in range(0,len(lst)):
     avg=(max+min)//2
     lst[i]=avg
print(lst)
