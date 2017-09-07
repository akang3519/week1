secret = 4;

for i in range(0,3):
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("You guessed correctly!")
        break;
    elif guess != secret:
        print("Incorrect Guess")
        break;

