import random

secret = random.randint(1,30)
tries = 0
print("I'm thinking of a number between 1 and 30.")
while True:
    try:
        guess = int(input("Your Guess: "))
    except ValueError:
        print("Numbers Only please!")
        continue
    tries +=1

    if guess<secret:
        print("Too Low,Try again Nigga!")
    elif guess > secret:
        print("Too High,Nigga :)")
    else:
        if tries == 1:
            print(f"Legend! You got it in {tries} try! 🏆")
        else:
            if tries <=5:
                print(f"Impressive You got it in {tries} tries.")
            else:
                print(f'Correct!You got it in {tries} Tries Nigga!!!!')
        break