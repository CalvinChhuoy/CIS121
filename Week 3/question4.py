age = int(input("Enter your age: "))
athleticism = input("Is your athleticism above average or below average: ")

if age >= 20 and age <= 39:
    if athleticism == "above average":
        print("Your resting heart rate is 47-42")
    else:
        print("Your resting heart rate is 73-93")
if age >= 40 and age <= 59:
    if athleticism == "above average":
        print("Your resting heart rate is 46-71")
    else:
        print("Your resting heart rate is 72-94")
if age >= 60 and age <= 79:
    if athleticism == "above average":
        print("Your resting heart rate is 45-70")
    else:
        print("Your resting heart rate is 71-97")
    