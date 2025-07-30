import random
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
        return words
def is_valid_guess(guess,guesses):
    return guess in guesses
def evaluate_guess(guess,word):
    str = ""
    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        else :
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i]
    return str + "\033[0m"
def wordle(guesses,answers):
    print("The Wordle gods await your offering…")
    print("Five letters. Six tries. Infinite glory...")
    print("Let the letter-hunt begin!")
    secret_word = random.choice(answers)
    attempts = 1
    max_attempts = 6
    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ":" ).lower()
        if not is_valid_guess(guess,guesses):
            print("Invalid guess.Please enter an english word with five letters!")
            continue
        if guess == secret_word:
            print("CONGRATULATIONS!! YOU GUESSED THE WORD CORRECTLY!!!")
            break
        attempts +=1
        feedback = evaluate_guess(guess,secret_word)
        print(feedback)
    if attempts > max_attempts:
        print("GAME OVER! THE SECRET WORD WAS:",secret_word)
guesses = load_dictionary("guess.txt")
answers = load_dictionary("answers.txt")
wordle(guesses,answers)
