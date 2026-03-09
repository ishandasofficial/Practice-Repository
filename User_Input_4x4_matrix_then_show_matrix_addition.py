# Program to add two 4x4 matrices using user input

# Initialize matrices
matrix1 = []
matrix2 = []
result = []

print("Enter elements for Matrix 1 (4x4):")
for i in range(4):
    row = []
    for j in range(4):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)

print("\nEnter elements for Matrix 2 (4x4):")
for i in range(4):
    row = []
    for j in range(4):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

# Matrix Addition
for i in range(4):
    row = []
    for j in range(4):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Display Matrix 1
print("\nMatrix 1:")
for row in matrix1:
    print(row)

# Display Matrix 2
print("\nMatrix 2:")
for row in matrix2:
    print(row)

# Display Result
print("\nMatrix Addition (Result):")
for row in result:
    print(row)