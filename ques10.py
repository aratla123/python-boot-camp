''' print the element in a particular index by cyclic printing
testcase:1
k=3
3,6,,8,4,61,2
o/p:4
testcase2:
k=8
80,70,54,36,72
o/p:54 '''

lst=list(map(int,input().split()))
k=int(input())
for i in range(0,len(lst)):
    rem=k%(len(lst))
print(lst[rem])