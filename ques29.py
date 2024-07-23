#peak element

'''lst=list(map(int,input().split()))
peak=0
count=0
for i in range(1,len(lst)-1):
    if(lst[i-1]<lst[i] and lst[i]>lst[i+1]):
      count=i
      break
print(lst[count])
peak=lst[i]
print(peak)'''

#method =2
'''peak=0
count=0
for i in range(1,len(lst)-1):
    if(lst[i-1]<lst[i] and lst[i]>lst[i+1]):
      #count=i
      #break
      print(lst[i],end=" ")
#peak=lst[i]
#print(peak)'''

#method 3:
'''peak=0
#count=1
for i in range(1,len(lst)-1):
    if(lst[i-1]<lst[i] and lst[i]>lst[i+1]):
      #count=i
      #break
#print(lst[count])
       peak=lst[i]
print(peak)'''

#method 4
'''lst=list(map(int,input().split()))
count=0
for i in range(1,len(lst)-1):
    if(lst[i]>lst[i-1] and lst[i]>lst[i+1]):
      count=i
      #break
      #print(lst[i],end=" ")
if(lst[-1]>lst[-2] and lst[-1]>count):
         count=len(lst)-1
print(lst[count])
#peak=lst[i]
#print(peak)'''