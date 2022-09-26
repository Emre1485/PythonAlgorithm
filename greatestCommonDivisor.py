numA = int(input("Enter the first number: "))
numB = int(input("Enter the second number: "))

while numA != numB:
    if numA > numB:
        numA = numA - numB
    else:
        numB = numB - numA
print(numA)