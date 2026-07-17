import numpy as np

marks=np.random.randint(40,101,size=(5,3))

print(marks)

print("Shape : ",marks.shape)

print("Subject-wise mean : ",np.mean(marks,axis=0))
print("Subject-wise mean :",np.mean(marks,axis=1))