import numpy as np

a=np.arange(9,dtype=np.float64).reshape(3,3)
print("first array:")
print(a)

b=np.array([10,10,10])
print("second array:")
print(b)

print("Add two arrays:")
print(np.add(a,b))

print("Subtract two arrays:")
print(np.subtract(a,b))

print("Multiply two arrays:")
print(np.multiply(a,b))

print("Divide two arrays:")
print(np.divide(a,b))






