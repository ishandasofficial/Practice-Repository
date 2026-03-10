# Program to input two 2D arrays (8 elements) and multiply them

A = []
B = []
result = []

rows = 2
cols = 4

print("Enter elements for First 2D Array:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for A[{i}][{j}]: "))
        row.append(element)
    A.append(row)

print("\nEnter elements for Second 2D Array:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for B[{i}][{j}]: "))
        row.append(element)
    B.append(row)

print("\nFirst Array:")
for i in A:
    print(i)

print("\nSecond Array:")
for i in B:
    print(i)

# Array multiplication (element-wise)
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] * B[i][j])
    result.append(row)

print("\nMultiplication of Arrays:")
for i in result:
    print(i)