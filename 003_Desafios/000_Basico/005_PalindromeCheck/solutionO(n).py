# tempo O(n)
# espaco/memoria O(n)

def manually_way(string):
    string_reverse = ''
    for index in reversed(range(len(string))):
        string_reverse += string[index]

    return string_reverse == string


def reverse_string(string):
    string_reverse = string[::-1]

    return string_reverse == string


def another_reverse_string(string):
    string_reverse = ''.join(reversed(string))

    return string_reverse == string


print(manually_way("abccba"))
