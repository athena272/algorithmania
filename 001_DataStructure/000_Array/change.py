def line():
    print("=============================")


# change values
print("Change Values | Temporary Variables")
a = [1, 2, 3, 4]
print(a)
tmp1 = a[1]
tmp2 = a[2]
a[2] = tmp1
a[1] = tmp2
print(a)

line()

print("Change Values | Fast Way")
a = [1, 2, 3, 4]
print(a)
a[2], a[1] = a[1], a[2]
print(a)
