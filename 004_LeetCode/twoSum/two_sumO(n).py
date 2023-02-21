def median_two_sum(target, array, calc_numbers={}):
    for number in array:
        golden_ticket = target - number

        if golden_ticket in calc_numbers:
            # return [golden_ticket, number]
            return [array.index(golden_ticket), array.index(number)]

        calc_numbers[number] = True

    return []

target = 9
array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
array2 = [4, 1, 2, -2, 11, 16, 1, -1, -6, -4]


print(median_two_sum(target, array))
print(median_two_sum(target, array2))