a = [34, 35, 37, 36, 40, 39]
n = len(a)

for i in range(n):
     
    for j in range(0, n-i-1):
        if a[j]>a[j + 1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t

print(a)