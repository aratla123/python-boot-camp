# password verifier
''' mr x is trying to create a new password for his instagram account these are required conditions for creating a new password
cond1:min length=8 and max length=15
cond2:only @,/ are allowed in a password
cond3:no spaces are allowed
cond4:only alpha numerics are allowed
u are suppose to print weak if length is exact 8 
medium lengthis b/w 8 to 12,
strong length is b/w 12 to 15'''

n=input()
l=len(n)
a="@" or "/"
for i in a:        
    if " " not in n:
        if(l==8):
            print("week password")
        elif(l>8 or l==12):
            print("medium password")    
        elif(l>12 or l==15):
            print("strong password")
    else:
        print("please follow all the conditions")

    
