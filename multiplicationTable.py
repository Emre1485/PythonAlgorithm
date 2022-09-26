numX = int(input("Enter number x: "))
numY = int(input("Enter number y: "))

for i in range(1, numX + 1):
    for j in range(1, numY + 1):
        print(i , " x ", j, " = ", i * j)