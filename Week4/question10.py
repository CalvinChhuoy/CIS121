big = 0 
num=0
while num>=0:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        if num > big:
            big = num
if big == 0:
    print("Largest -1")
else:
    print(big)
            