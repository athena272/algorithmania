# target = 9
# array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
# answer = -2 | 11 = 9

# O(n log n)
# > target: Move ponteiro direita
# < target: Move ponteiro esquerda
# = target: Move os dois ponteiros

def best_two_sum(target, array):
    array.sort()

    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:

        golden_ticket = array[left_pointer] + array[right_pointer]

        if golden_ticket == target:
            return [array[left_pointer], array[right_pointer]]

        elif golden_ticket < target:
            left_pointer += 1

        elif golden_ticket > target:
            right_pointer -= 1

    return []


target = 9
array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
array2 = [4, 1, 2, -2, 11, 16, 1, -1, -6, -4]

print(best_two_sum(target, array))
print(best_two_sum(target, array2))

