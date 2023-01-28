def factorial(maxNumber):
  for each in range(maxNumber):
    print(each)
    factorial(maxNumber - 1)
    
factorial(5)