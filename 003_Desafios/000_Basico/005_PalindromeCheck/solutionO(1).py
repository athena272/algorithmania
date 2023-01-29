# tempo O(n)
# espaco/memoria O(1)

def best_palindrome(string):
    last_index = len(string) - 1
    for index in range(len(string)):
        if last_index == index:
            return True

        if string[index] != string[last_index]:
            return False

        last_index -= 1

    return True

print(best_palindrome('abcba'))

print(best_palindrome('level'))

print(best_palindrome('agjgwneogoa'))
