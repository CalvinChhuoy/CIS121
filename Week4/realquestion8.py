user_num = int(input("Enter a number: "))
for i in range (1, user_num+1):
    if user_num % i == 0:
        print(i)