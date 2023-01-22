import copy


def line():
    print("=============================")


# Shallow Copy
print("Shallow Copy")
A = [1, 2, 3]
B = A
B[0] = 999
print(A, B)

line()

# Deep Copy
print("Deep Copy")
a = [1, 2, 3]
b = list(a)
b[0] = 999
print(a, b)

line()

# Example
print("Library Copy | Shallow Copy")
a = [{'test': 123, 'bbb': 456}]
b = copy.copy(a)
b[0]['test'] = 999
print(a, b)

line()

print("Library Copy | Deep Copy")
a = [{'test': 123, 'bbb': 456}]
b = copy.deepcopy(a)
b[0]['test'] = 999
print(a, b)

line()


