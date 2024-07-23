#mr.z selected for olympics, he is selected in swimming,x,y are friends of z
#     x is participating in badminton
# y is participating in table tennis
# according to selection committe requirements for badminton are 1.height=140cm,weight =factor of 2,body fat<12%
# table tennies ==1 height=118cm to 148cm,wight=factors of number of medals won by mr z,bodyfat=14%,according to
# the previous history z participated in 14 game out of which he is having succes rate as 65%,

# write a program to check wheather mrz,mrx,mry from india travel in a same plain or not
#print("swimming","badminton","table tennis")
height=int(input())
weight=int(input())
body_fat=int(input()) 
if(height>140 and weight=(weight%2==0) and body_fat<12):
    print("x is selected for badminton")
    x=True 
h2=int(input())
w2=int(input())
bf2=int(input())
if((h2>118 and h2<148) and w2=w2%((65/100)*14)==0 and bf2<14):
    print("y is selected for table tennies")
    y=True
if(x==True and y==True):
    print("x,y,z travel in same plain")
else:
    print("x,y,z does not travel in a same plain")  


                        


