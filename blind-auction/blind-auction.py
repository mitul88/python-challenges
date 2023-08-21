import os
print("Welcome to the blind auction program")
bider = {}
def ask():
    name = input("What is your name?")
    bid = int(input("How much you want to bid?"))
    bider[name] = bid
    cont = input('Is there anyone else to bid? "yes"/"no"?').lower()

    if cont == "yes":
        os.system('cls')
        ask()
    elif cont == "no":
        max_bider = max(bider)
        print(f'the highest bidder is {max_bider} with bid amount of {bider[max_bider]}')
    else:
        print('Please type "yes" or "no" to continue')
        ask()
            
ask()

print(f'all biders: {bider}')
