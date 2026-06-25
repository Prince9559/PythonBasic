n=7 
for i in range(n):

    for j in range(n):

        condition = j==0 or j==6 or i==j and i<=3 or i+j==6 and i<=3
         
        if condition:
            print(" *",end="")

        else:

            print("  ",end="")    

    print()        