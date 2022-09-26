# Find How Many Of The 10 Numbers Entered Are Positive, Negative and Zero.
num = 0
count = 0
pozNum = 0
negNum = 0
numZero = 0
for num in range (1, 11):
    num = int(input("Enter a number: "))
    if num > 0:
        pozNum = pozNum + 1
    elif num < 0:
        negNum = negNum + 1
    else:
        numZero = numZero + 1

print(" ", pozNum, " positive number ", negNum, " negative number and ", numZero, " of them zero")