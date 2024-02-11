from cs50 import get_int

import random

word_dict ={
    'Animals': ['dog', 'cat', 'elephant', 'lion', 'tiger', 'zebra', 'giraffe', 'monkey', 'penguin', 'dolphin',
                'snake', 'parrot', 'rabbit', 'kangaroo', 'octopus', 'panda', 'cheetah', 'koala', 'hippo', 'fox'],

    'Countries': ['usa', 'canada', 'australia', 'germany', 'japan', 'brazil', 'russia', 'china', 'india', 'france',
                  'italy', 'mexico', 'korea', 'spain', 'argentina', 'britain', 'egypt', 'vietnam', 'nigeria', 'kenya'],

    'Sports': ['soccer', 'basketball', 'tennis', 'golf', 'cricket', 'rugby', 'swimming', 'volleyball', 'baseball', 'boxing',
               'cycling', 'skiing', 'surfing', 'wrestling', 'hockey', 'badminton', 'athletics', 'table tennis', 'weightlifting', 'rowing']}

def main():
    playername = input("Enter player name: ")
    total_score = 0
    selection = menu()
    while True:
        if selection == 1:
            print_hangman_instructions()
            check = True
            while check:
                temp = input("Enter m to return menu ")
                temp = str(temp)
                try:
                    if temp == "m":
                        check = False
                        selection = menu()
                except:
                    print("Invalid input, try again.")

        elif selection == 2:
            word_list = word_dict['Animals']
            random_word = random.choice(word_list)
            print("Category: Animals")
            attempts= play_hangman(random_word)
            total_score += attempts * 5
            check = True
            while check:
                temp = input("Enter m to return menu ")
                temp = str(temp)
                try:
                    if temp == "m":
                        check = False
                        selection = menu()
                except:
                    print("Invalid input, try again.")
        elif selection == 3:
            word_list = word_dict['Countries']
            random_word = random.choice(word_list)
            print("Category: Countries")
            attempts= play_hangman(random_word)
            total_score += attempts * 5

            check = True
            while check:
                temp = input("Enter m to return menu ")
                temp = str(temp)
                try:
                    if temp == "m":
                        check = False
                        selection = menu()
                except:
                    print("Invalid input, try again.")
        elif selection == 4:
            word_list = word_dict['Sports']
            random_word = random.choice(word_list)
            print("Category: Sports")
            attempts= play_hangman(random_word)
            total_score += attempts * 5

            check = True
            while check:
                temp = input("Enter m to return menu ")
                temp = str(temp)
                try:
                    if temp == "m":
                        check = False
                        selection = menu()
                except:
                    print("Invalid input, try again.")
        elif selection == 5:
            category = random.choice(list(word_dict.keys()))
            word_list = word_dict[category]
            random_word = random.choice(word_list)
            print(f"Random category: {category}")
            attempts= play_hangman(random_word)
            total_score += attempts * 5

            check = True
            while check:
                temp = input("Enter m to return menu ")
                temp = str(temp)
                try:
                    if temp == "m":
                        check = False
                        selection = menu()
                except:
                    print("Invalid input, try again.")
        elif selection == 6:
            print("Scoreboard: ", total_score)
            check = True
            while check:
                temp = input("Enter m to return menu ")
                temp = str(temp)
                try:
                    if temp == "m":
                        check = False
                        selection = menu()
                except:
                    print("Invalid input, try again.")
        else:
            print(playername + " scored", str(total_score) + " points in total")
            print("Exiting program...")
            break

def menu():
    print("")
    print("")
    print("╔═════════════════════════════════════════════════╗")
    print("║                Welcome to Hangman!              ║")
    print("║                                                 ║")
    print("║ 1. Instructions (recommended for new players)   ║")
    print("║ 2. Animals                                      ║")
    print("║ 3. Countries                                    ║")
    print("║ 4. Sports                                       ║")
    print("║ 5. Random Category                              ║")
    print("║ 6. Scoreboard                                   ║")
    print("║ 7. Exit                                         ║")
    print("╚═════════════════════════════════════════════════╝")
    print("")
    print("")
    check = True
    while check:
        selection = get_int("Number: ")
        try:
            if selection > 0 and selection < 8:
                check = False
        except:
            print("Invalid input, try again")
    return selection

def print_hangman_instructions():
    print("Here are the instructions:")
    print("1. Choose a category provided in the main menu")
    print("2. A secret word is chosen, and the length of the word is shown as blanks.")
    print("3. You have to guess letters one at a time to fill in the blanks.")
    print("4. If the letter you guessed is in the word, all occurrences of that letter are revealed.")
    print("5. If the letter you guessed is not in the word, you lose a life.")
    print("6. If you decide to guess the whole word instead of a letter, you lose a life if the guess is not exactly the same as the secret word.")
    print("7. The game ends when you guess the word correctly or run out of lives.")
    print("Good luck and have fun!")

def play_hangman(random_word):
    word_length = len(random_word)
    attempts = word_length - 1
    guessed_word = ['-' for _ in range(word_length)]  # Initialize guessed word with dashes
    correct_guesses = set()  # Set to store correct guesses

    print("Try to guess the word in the selected category.")
    print("You have", attempts, "attempts.")

    while attempts > 0:
        print("Current word:", ''.join(guessed_word))
        guess = input("Enter a letter or guess the whole word: ").strip().lower()

        if len(guess) == 1:  # Guessing a single letter
            if guess in correct_guesses:
                print("You've already guessed this letter.")
            elif guess in random_word:
                print("Correct guess!")
                correct_guesses.add(guess)
                for i, letter in enumerate(random_word):
                    if letter == guess:
                        guessed_word[i] = letter
                if '-' not in guessed_word:
                    print("Congratulations! You've guessed the word:", random_word)
                    return attempts
            else:
                print("Incorrect guess.")
                attempts -= 1
        elif len(guess) == word_length:  # Guessing the whole word
            if guess == random_word:
                print("Congratulations! You've guessed the word:", random_word)
                return attempts
            else:
                print("Incorrect guess.")
                attempts -= 1
        else:
            print("Invalid input. Please enter a single letter or the entire word.")

        print("Attempts left:", attempts)

    print("Out of attempts! The word was:", random_word)
    return 0


main()
