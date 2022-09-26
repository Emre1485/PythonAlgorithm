num = int(input("Enter a number: "))
primeNum = 0
count = 2
for count in range(2, int(num/2 + 1)):
    
    if num % count == 0:
        primeNum = 1

if num < 2:
    print(num, " is not a prime number")
else:
    if primeNum == 0:
        print(num, " is a prime number")
    else:
        print(num, " is not a prime number")
