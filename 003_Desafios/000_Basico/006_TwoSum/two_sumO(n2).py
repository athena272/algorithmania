# target = 9
# array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
# answer = -2 | 11 = 9

# def worst_two_sum(target, array):
#     for i in array:
#         for j in array:
#             if target == (i + j):
#                 return [i, j]

#     return False
# def worst_two_sum(target, array):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):

#             if target == (array[i] + array[j]):
#                 return [array[i], array[j]]

#     return False
def worst_two_sum(target, array):
    for number1_index in range(len(array)):
        number1 = array[number1_index]

        for number2_index in range(number1_index + 1, len(array)):
            number2 = array[number2_index]

            if target == (number1 + number2):
                return [number1, number2]

    return []

target = 9
array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]

print(worst_two_sum(target, array))
