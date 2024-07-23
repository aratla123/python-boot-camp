my_list=list(map(int,input().split(",")))
print("enter the choice:\n")
print("1.append 2.pop  3.sort 4.length of a list\n")
choice=int(input())
if(choice==1):
     my_list.append(int(input()))
     print(my_list)
elif(choice==2):
     my_list.pop(4)
     print(my_list)
elif(choice==3):
     my_list.sort()
     print(my_list)
elif(choice==4):
     print(len(my_list))
else:
     print("exit")