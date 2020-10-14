
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("I am thinking of a secret word. Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN!")

secret_number = "10"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("i am thinking of a secret number. Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN")
