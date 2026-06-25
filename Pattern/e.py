n=7 

for i in range(n):

    for j in range(n):

        condition =j==0 or i==0 or i==3 or i==n-1

        if condition:
            print(" *",end="")
        else:
            print("  ",end="")

    print()        