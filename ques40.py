#print the unique characters in a string(non repeating characters)

inp=str(input())
str="aeioubcdfghjklmnpqrstvwxyz"
ans=""
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)

