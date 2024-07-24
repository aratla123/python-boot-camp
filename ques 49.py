# uppercase triangle

'''for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print()'''

    #uppercase triangular matrix

# Function to form upper triangular matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3): 
      for j in range(0,3): 
           if (i > j): 
              print("0", end = " "); 
           else: 
                print(matrix[i][j],end = " " ); 
      print(" ")
      
