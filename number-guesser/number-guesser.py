def number_guesser():
    import random

    random_num = random.randint(1, 100)

    print("Welcome to number guessing app")
    print("I am thinking of a number fromt 1 to 100, can you guess it ? ")

    attempt = 0

    difficulty = input('Please chose your difficulty level. type "hard" or "easy"').lower()

    if difficulty == "hard":
        attempt = 5
    elif difficulty == "easy":
        attempt = 10
    else:
        print('please type "hard" or "easy"')
        number_guesser()

    print(f'you have {attempt} attempts remaining')

    for i in range(attempt):
        guess = int(input("Enter guess: "))
        if guess == random_num:
            print(f"Your guess {guess} is right. Congratulations!!")
            print("You win")
            break;
        else:
            if guess > random_num:
                print("correct answer is smaller")        
            if guess < random_num:
                print("correct answer is greater")
            if i == attempt-1:
                print("you have no more guess left")
                restart = input("Do you want to restart ? Y/N ?")
                if restart == "Y" or restart == "y":
                    print("Game restarted")
                    number_guesser()
                elif restart == "N" or restart == "n":
                    print("Game over")
                    break;
                
        
            print(f"Incorrect. You have {attempt} guess left")
    

number_guesser()