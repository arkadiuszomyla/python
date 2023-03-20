i = 1
iMax = 10

while i <= iMax:
    print(i, "I like Python")
    i += 1
else:
    print("Now i =", i)

i = 1
# 5*'x'
while i <= iMax:
    print(i * 'x')
    i += 1

values = [10, 43, 12, 48, 12, 11, 18, 98, 57, 28, 19, 27, 49, 19, 74]
i = 0
max = len(values) - 3

while i < max:
    print(i, values[i], values[i + 1], values[i + 2])
    i += 1
    if values[i] < values[i + 1] and values[i + 1] < values[i + 2]:
        print("\tFound: ", values[i], values[i + 1], values[i + 2])

