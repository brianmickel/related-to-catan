import numpy as np

myArray = np.array([[[ 0, 1, 2,],
[ 3, 4, 5,],
[ 6, 7, 8,]],

[[ 9, 10, 11,],
[ 12, 13, 14,],
[ 15, 16, 17,]],

[[ 18, 19, 20,],
[ 21, 22, 23,],
[ 24, 25, 26,]]]
)

print(myArray)
print(myArray[0])
print(myArray[1])
print(myArray[2])
print(myArray[0,0,0])
print(myArray[0,1,0])
print(myArray[0,0,1])
print(myArray[1,0,0])

resources = {0:'ore',1:'lumber'}

print(resources[1])

# top left to bottom right
coordinates =[
[0,2,-2],
[1,1,-2],
[2,0,-2],
[-1,2,-1],
[0,1,-1],
[1,0,-1],
[2,-1,-1],
[-2,2,0],
[-1,1,0],
[0,0,0],
[1,-1,0],
[2,-2,0],
[-2,1,1],
[-1,0,1],
[0,-1,1],
[1,-2,1],
[-2,0,2],
[-1,-1,2],
[0,-2,2]
]
