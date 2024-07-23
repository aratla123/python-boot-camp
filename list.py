# my_list=[1,2,9,4]
# my_list.append(9999)   #append:inserts at the end
# my_list.insert(1,9999)  #insert:inserts in a specified position
# print(len(my_list))  #prints the size of list
# my_list.pop()   #default pops the last element
# my_list.pop(2)  #pop the specified element
# print(*my_list,end=" @")   #(*)eliminates the square braceses with commas
# my_list_2=[5,6,7,8]
# new_lst=my_list+my_list_2    #"+" concatinates the string
# print(*new_lst)
# new_lst=my_list.copy()
# new_lst.pop()
# print(*new_lst)/
#cnt=my_list.count(2)  #ocurrences of 2 in a given list
#print(cnt)
# my_list.sort()
# print(my_list)
# my_list=list(map(int,input().split("@")))    #list=typecast , split("") = space seperator using slip function ,map=takes more than one input
# print(*my_list)                           #split("@")=@seperator,split(",")=comma seperater,split("")=default seperator etc..  
                                          #1@2@3@4=1 2 3 4 ,     1,2,3,4=1 2 3 4 ,          1,2,3,4= 1 2 3 4
# my_list=list(map(str,input().split("@")))    
# print(*my_list)       '''pop will not work for str'''

# my_list=list(map(int,input().split(",")))
# print("enter the choice:\n")
# print("1.append 2.pop  3.sort 4.length of a list\n")
# choice=int(input())
# if(choice==1):
#      my_list.append(int(input()))
#      print(my_list)
# elif(choice==2):
#      my_list.pop(4)
#      print(my_list)
# elif(choice==3):
#     my_list.sort()
#     print(my_list)
# elif(choice==4):
#     print(len(my_list))
# else:
#     print("exit")

# my_list=list(map(int,input().split()))
# for i in range(len(my_list)):
#      print(my_list[i],end=" ")
#      print("\n------------------------")
#      for i in my_list:
#          print(i,end= ",")

# s="hello world"
# for i in range(len(s)):
#     print(s[i],end=" ")

# s="hello world"
# for i in range(len(s)):
#      print(s[i],end=" ")
#      print()
     