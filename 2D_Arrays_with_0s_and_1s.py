# Program to input and display a 2D array with 0 and 1 values (10 elements)

rows = 2
cols = 5

matrix = []

print("Enter 10 elements (only 0 or 1):")

for i in range(rows):
    row = []
    for j in range(cols):
        while True:
            val = int(input(f"Enter element [{i}][{j}]: "))
            if val == 0 or val == 1:
                row.append(val)
                break
            else:
                print("Invalid input! Please enter only 0 or 1.")
    matrix.append(row)

print("\nThe 2D Array is:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()


# Display original matrix
print("\nThe 2D Array is:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

# ---- Sequel Part (Conversion) ----

# Convert 0 to 1 and 1 to 0
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = 1 - matrix[i][j]

# Display updated matrix
print("\nMatrix after conversion (0 ↔ 1):")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

# ---- Sequel Part (Positions of 1s) ----

print("\nPositions with value 1:")

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1:
            print(f"Position [{i}][{j}]")
            