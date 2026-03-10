# Program for 1D and 2D Array using 10 elements

# 1D Array
array_1d = []

print("Enter 10 elements for 1D Array:")

for i in range(1, 11):
    element = int(input(f"Enter element {i}: "))
    array_1d.append(element)

print("Your 1D Array is:", array_1d)


# 2D Array (2x5 = 10 elements)

rows = 2
cols = 5

array_2d = []

print("\nEnter 10 elements for 2D Array:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for row {i+1} column {j+1}: "))
        row.append(element)
    array_2d.append(row)

print("\nYour 2D Array is:")
for row in array_2d:
    print(row)

