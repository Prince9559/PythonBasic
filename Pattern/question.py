n=7

for i in range(n):

    for j in range(n):

        condition =  i==j or i+j==i or i==6 and j+1<=4

        if condition:
            print(" *", end="")
        else:
            print(" ",end="")

    print()        