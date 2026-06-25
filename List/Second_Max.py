a=[90,390,22,122]

max1=max(a)
max2=0

for x in a:

    if x !=max1 and x>max2:
        max2=x

print("Max : ",max2)
