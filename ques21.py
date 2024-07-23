lst=list(map(int,input().split()))
max1=lst[0]
for i in range(len(lst)):
    if max<lst[i]:
        max1=lst[i]
max2=0
for i in range(len(lst)):
    if lst[j] != max1 and max2 < lst[j]:
        max2=lst[j]
print(max2)
