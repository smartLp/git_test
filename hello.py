import numpy as np

a = np.array([1,2,3])
b = 3
c = a*b
print(c)
d = np.random.random(1,2)
print(d)
# print the bigger one 
def operation(a,b):
    if a > b:
        print (a)
    else:
        print(b)
