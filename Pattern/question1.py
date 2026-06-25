n=7

for i in range(n):

    for j in range(n):

        condition = i>=j

        if condition:
            print(" *" ,end="")
        else:
            print("  " ,end="")

    print("",end="")

    for j in range(n):

        condition = i+j>=6

        if condition:
            print(" *",end="")

        else:

            print("  ",end="")

    print()                