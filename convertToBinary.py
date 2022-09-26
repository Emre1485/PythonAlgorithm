# Convert decimal (Base 10) numbers to binary

num = int(input("Enter a number: "))
remainder = 1
baseTwo = " "
while num > 1:
    remainder = num % 2
    num = int(num/2)
    baseTwo = str(remainder) + baseTwo
baseTwo = "1" + baseTwo
print(baseTwo)