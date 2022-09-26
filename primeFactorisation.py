num = int(input("Enter a number: "))
primeDiv = 2

while num > 1:
    if num % primeDiv == 0:
        num = num / primeDiv
        print(primeDiv)
    else:
        primeDiv = primeDiv + 1