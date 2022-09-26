# Second Degree Equasition Solution

numA = float(input("Enter coefficent A"))
numB = float(input("Enter coefficent B"))
numC = float(input("Enter coefficent C"))
x1 = 1
x2 = 1
delta = (float(numB) ** 2) - (4 * float(numA) * float(numC))

if delta < 0:
    print("Equasition has no root")

elif delta > 0:
    x1 = (-numB + (delta)**(1/2)) / (2 * numA)
    x2 = (-numB - (delta)**(1/2)) / (2 * numA)
    print("Equasition has 2 roots: " , x1 , " and " , x2)

else:
    x1 = -numB / (2 * numA)
    print("Equasition has 1 root: " , x1)
