'''find the maximum element in a given list without max function
testcase:0
12 23 36 44 45 57

testcase:1
56 78 -8 12 34 -99
78'''

lst=list(map(int,input().split()))
a=0
for i in range(0,len(lst)):

    if(lst[i]>a):
     a=lst[i]
    
print(a)