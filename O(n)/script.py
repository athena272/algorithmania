def printItems(myArray):
  for item in myArray:
    print(item)
    
def findMax(myArray):
  max = myArray[0]
  for item in myArray:
    if (item > max):
      max = item
  
  return max