num = int(input("Enter a number"))
count = 1
factorial = 1
for count in range(1, num + 1):
    factorial = factorial * count
print(factorial)