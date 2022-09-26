num = int(input("Enter a number: "))
sumOfFactors = 0
count = 1
for count in range(1, int(num/2 + 1),1):
    
    if num % count == 0:
        sumOfFactors += count

if num == sumOfFactors:
    print(num, " is a perfect number!")
else:
    print(num, " is not a perfect number!")