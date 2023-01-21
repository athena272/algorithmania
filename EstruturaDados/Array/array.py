import bisect

myArray = [-1, 2, 3, 5, 456]

print(bisect.bisect(myArray, 5))
bisect.insort(myArray, 888)
print(myArray)