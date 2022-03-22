import random
Rand_No = random.randint(1,100)
User_No = None
Guess = 1
while (User_No!=Rand_No):
    User_No = int(input("Guess A Number Between 1 To 100: "))
    if User_No>Rand_No:
        print("Your Guess is Too High")
        print("Guess Any Smaller Number")
    elif User_No<Rand_No:
        print("Your Guess is Too Low")
        print("Guess Any Higher Number")
    elif User_No == Rand_No:
        print(f"Congratulations, You Guessed {User_No} : It is a perfect Guess")
        print(f"You Take {Guess} times to Guess Correct")
        break
    Guess = Guess+1