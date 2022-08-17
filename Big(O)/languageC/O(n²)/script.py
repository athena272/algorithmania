def findCommonItems(list1, list2):
  result = []
  for item1 in list1:
    for item2 in list2:
      if (item1 == item2):
        result.append(item1)
  
  return result

list1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
list2 = [0, 3, 6, 9, 12, 15, 18, 21]
print(findCommonItems(list1, list2))