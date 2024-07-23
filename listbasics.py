my_list=[1,2,9,4]
my_list.append(9999)   
my_list.insert(1,9999)  
print(len(my_list))  
my_list.pop()   
my_list.pop(2)  
print(*my_list,end=" @")   
my_list_2=[5,6,7,8]
new_lst=my_list+my_list_2    
print(*new_lst)
new_lst=my_list.copy()
new_lst.pop()
print(*new_lst)
cnt=my_list.count(2)  
print(cnt)
my_list.sort()
print(my_list)
my_list=list(map(int,input().split("@")))    
print(*my_list)  
         