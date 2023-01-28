def dynamic_fibonacci(number, memory={}):
    if number == 1 or number == 2:
        return 1

    if number not in memory:
        memory[number] = dynamic_fibonacci(
            number - 1) + dynamic_fibonacci(number - 2)

    return memory[number]
