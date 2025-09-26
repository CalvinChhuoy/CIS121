secret_num = 67
user_num = 0
while user_num != 67:
    user_num = int(input("Guess the secret number: "))
    if user_num > 67:
        print("Too high")
    elif user_num < 67:
        print("Too low")
    elif user_num == 67:
        print("CONTRATS WHO GIVES A FUCK.")    