# tempo O(n)
# espaco/memoria O(1)

def best_palindrome(string):
    last_index = len(string) - 1
    for index in range(len(string)):
        if string[index] != string[last_index]:
            return False

        last_index -= 1