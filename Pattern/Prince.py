n=7

for i in range(n):

    for j in range(n):

        condition = i==0 or j==0 or j==6 and i<=3 or i==3

        if condition:
            print(" *",end="")
        else:
            print("  ",end="")

    print(" " ,end=" ")
 



    for j in range(n):

        condition = i==0 or j==0 or j==6 and i<=3 or i==3 or i-j==2
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print(" ",end=" ")  


    for j in range(n):
        condition = i==0 or i==6 or j==3    
        if condition:
            print(" *", end="")
        else:
            print("  ",end="")

    print(" ",end=" ")       

 
    for j in range(n):
        condition = j==0 or j==6 or i==j
        if condition:
            print(" *", end="")   

        else:
            print("  ",end="")

    print(" ",end=" ")     


    for j in range(n):
        condition =j==0 and i>=1 or i==0 or i==6

        if condition:
            print(" *",end="")
        else:
            print("  ",end="")

    print(" ",end=" ")          

    for j in range(n):
        condition = i==0 or i==6 or j==0 or i==3
        if condition:
            print(" *", end="")

        else:

            print("  ",end="")    
    print()          