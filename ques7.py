#given with a comma seperated natural numbers 1to 10 print only the even numbers
'''my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    print(my_list[i])'''
#frequency of even numbers
'''my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
    count+=1
print(count)'''

#given with a space seperated integer list, find no.of even elements and no.of odd elements in agiven list
'''my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list)):  #i=index my_list[i]=value
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(odd)
print(even)'''
