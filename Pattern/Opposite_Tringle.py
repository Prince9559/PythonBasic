n=7

for i in range (n):

    for j in range(n):

        condition= j>=i

        if condition:

            print(" *", end="")

        else:

            print(" ", end="")

    print(" ",end=" ")  

    for j in range(n):

        condition= j>=n-1-i

        if condition:

            print(" *", end="")

        else:

            print(" ", end="")

    print()      