# target = 9
# array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
# answer = -2 | 11 = 9

# Tempo: O(n)
# Espaco/Memoria: O(n)

def median_two_sum(target, array, calc_numbers = {}):
    for number in array:
        golden_ticket = target - number

        if golden_ticket in calc_numbers:
            return [golden_ticket, number]

        calc_numbers[number] = True

    return []

target = 9
array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]

print(median_two_sum(target, array))