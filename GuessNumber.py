secret_number = 9
guess_count = 0
guess_limit = 3
print("Guess a number between 1 to 10.(GUESS LIMIT: 3)")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print('Sorry, you failed! :(')

