def slow_fibonacci(number):
    if number == 1 or number == 2:
        return 1

    return slow_fibonacci(number - 1) + slow_fibonacci(number - 2)
