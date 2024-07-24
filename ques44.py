# write a code to remove all the brackets from the algebraic expression

inp=str(input())
str="(){}[]"
for i in inp:
    if(i not in str):
         print((i))



         #method2
inp=str(input())
for i in inp:
    if(ord(i)==40  or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==125 or ord(i)==123):
         pass
    else:
         print(i,end="")
print()

