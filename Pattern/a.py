n=7

for i in range(n):

    for j in range(n):

        condition= j==0 and i>=1 or j==6 and i>=1 or i==0 and j>=1 and j<=5 or i==3

        if condition:
            print(" *",end="")

        else:
            print("  ",end="")

    print()        