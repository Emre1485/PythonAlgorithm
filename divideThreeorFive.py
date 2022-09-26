# List numbers that can be divided by 3 and 5 between 0-100 
num = 1
while num < 101:
    if num % 3 == 0 and num % 5 == 0:
        print(num, " Can be divided by 3 and 5")    
    num = num + 1