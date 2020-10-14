
secret_word = "travel"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("I am thinking of a secret word that involves a hobby I love. We can explore other countries by doing this activity. Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Sorry, you are out of guesses, YOU LOSE!")
else:
    print("COOL! YOU WON THIS CHALLENGE, BUT NOW IS THE SECOND CHALLENGE...")

secret_number = "10"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("I am thinking of a secret number. Its between 1 and 20. Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Sorry, you are out of guesses, YOU LOSE!")
else:
    print("AWESOME! YOU WIN")
