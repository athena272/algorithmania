def better_fibonacci(number):
    if number == 1 or number == 2:
        return 1

    memory = {0: 1, 1: 2, 2: 1}
    for i in range(2, number + 1):
        memory[i] = memory[i - 1] + memory[i - 2]

    return memory[number - 1]
