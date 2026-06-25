a=[900,800,600,400,300,100,1000,200,500]
n=len(a)

for i in range(n):

    for j in range(n-1-i):

        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t

print(a)        