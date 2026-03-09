#Write a python program of 1D, 2D Array using user input of 10 elements and show the all elements.

#1D Array
n = int(input("Enter the numbers of elements in the 1D array :: "))

array_1d = []
for i in range(1,n+1):
    element = int(input(f"Enter the {i}th element ::  "))
    array_1d.append(element)

print(f"Your 1D Array is :: ",array_1d)


#2D Array

rows = int(input("Enter the number of rows in the 2D array ::"))
cols = int(input("Enter the number of columns in the 2D array ::"))

array_2d = []
for a in range(1,rows+1):
    row = []
    for b in range(1,cols+1):
        element = input(f"Enter the element for row {a} and column {b} :: ")
        row.append(element)
    array_2d.append(row)

print(f"Your 2D Array is :: ",array_2d , end="")