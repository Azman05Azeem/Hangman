# IMPORTED LIBRARIES:
import random
import time


# FUNCTIONS:
def word_file_loader():  # LOADS WORDS FROM FILE

    # CHECKS IF FILE EXISTS OR NOT
    try:
        file = open("Wordlist.txt", "r")
        file.close()
    except FileNotFoundError:
        time.sleep(0.6)
        print("\n>> 'Wordlist.txt' Not found...")
        time.sleep(0.4)
        print(">>  Creating 'Wordlist.txt'")
        file = open("Wordlist.txt", "w")
        time.sleep(1)
        print(">> 'Wordlist.txt' Has been Created!")
        file.close()

    file = open("Wordlist.txt", "r")
    read_file_line = str(file.readline())

    # READING A FILE IF IT IS NOT EMPTY
    if read_file_line == "":
        time.sleep(0.7)
        print("\n==========================")
        print(">>> WORD FILE IS EMPTY <<<")
        print("==========================")
        print("\n>> Please Fill 'Wordlist.txt' to Continue...")
        file.close()

    else:
        # LOADS WORDLIST FROM FILE
        wordlist = []
        while True:
            wordlist.append(read_file_line)
            read_file_line = str(file.readline())
            if read_file_line == "":
                break
            elif ValueError:
                read_file_line = str(file.readline())

        # SELECTS RANDOM WORD FROM THE WORDLIST
        selected_word = random.choice(wordlist)
        file.close()
        main_game(selected_word)


def main_game(selected_word):  # MANAGES THE GAME

    word_length = len(selected_word)

    # DECIDES THE NUMBER OF HIDDEN WORDS
    if word_length <= 3:
        hidden_counts = 2
    else:
        hidden_counts = int((word_length / 2) + (word_length / random.randint(3, 4)))

    # DECIDES WHICH INDEX OF THE WORD TO HIDE
    hidden_index = random.sample(range(0, word_length), hidden_counts)
    hidden_index.sort()

    # ELIMINATING "SPACES" FROM THE INDEX LIST
    for index in range(word_length):
        if (selected_word[index] in [" ", "\n"]) and (index in hidden_index):
            hidden_index.remove(index)

    # HIDDEN CHARACTER'S LIST
    hidden_character_list_upper = []
    hidden_character_list_lower = []

    for index in range(word_length):
        if index in hidden_index:
            hidden_character_list_upper.append(selected_word[index].upper())
            hidden_character_list_lower.append(selected_word[index].lower())

    character_left = len(hidden_index)

    # GENERATING A CIPHERED STRING
    generated_string = ""

    for index in range(word_length):
        if index in hidden_index:
            generated_string += "_"
        else:
            generated_string += selected_word[index]

    # STRING DISPLAY
    time.sleep(0.5)
    print("\n>> Selecting a Word...")
    time.sleep(1.3)
    print(">> A Word has been Selected!")
    time.sleep(0.3)
    print("\n======================")
    print(">>> GUESS THE WORD <<<")
    print("======================")
    time.sleep(0.3)
    print("\n>> WORD: " + generated_string)

    # INPUT FROM USER, IN CASE OF WORD IT ONLY TAKES FIRST CHARACTER
    won = False
    attempts = 1

    while True:
        user_input_guess = input(">> Enter Your Guess: ")
        while user_input_guess == "":
            user_input_guess = input(">> Invalid Input!: ")
        user_input_guess = user_input_guess[0]

        # CHECKING THE VALUES
        if user_input_guess.upper() in hidden_character_list_upper:
            time.sleep(0.6)
            print("\n=====================")
            print(">>> CORRECT GUESS <<<")
            print("=====================")

            # REMOVE THE CHARACTER AND ITS INDEX FROM HIDDEN LIST
            while user_input_guess.upper() in hidden_character_list_upper:
                temp = hidden_character_list_upper.index(user_input_guess.upper())
                temp_a = hidden_index[temp]
                hidden_character_list_lower.remove(user_input_guess.lower())
                hidden_character_list_upper.remove(user_input_guess.upper())
                hidden_index.remove(temp_a)
                character_left -= 1

            # CREATING NEW CIPHER STRING
            generated_string = ""

            for index in range(word_length):
                if index in hidden_index:
                    generated_string += "_"
                else:
                    generated_string += selected_word[index]

            time.sleep(0.3)
            print("\n>> WORD: " + generated_string)

            if character_left == 0:
                won = True
                break
        else:
            time.sleep(0.5)
            graphics(attempts)
            attempts += 1
            if attempts > 7:
                break
            else:
                time.sleep(0.6)
                print("\n=======================")
                print(">>> INCORRECT GUESS <<<")
                print("=======================")
                time.sleep(0.3)
                print("\n>> WORD: " + generated_string)

    # SITUATIONS (WIN/LOSS)
    if won:
        time.sleep(0.6)
        print("======================================")
        print(">>> YOU CORRECTLY GUESSED THE WORD <<<")
        print("======================================")
    else:
        time.sleep(0.6)
        print("\n===================================")
        print(">>> YOU COULDN'T GUESS THE WORD <<<")
        print("===================================")
        print("\n>> The Word was: " + selected_word)


def graphics(select):  # HANG-MAN ANIMATIONS

    def hang_a():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print("/()\\__")

    def hang_b():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||       (=)")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print("/()\\__")

    def hang_c():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||       (=)")
        print(" ||        |")
        print(" ||        |")
        print(" ||        |")
        print(" ||        |")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print("/()\\__")

    def hang_d():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||       (=)")
        print(" ||       /|")
        print(" ||      / |")
        print(" ||        |")
        print(" ||        |")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print("/()\\__")

    def hang_e():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||       (=)")
        print(" ||       /|\\")
        print(" ||      / | \\")
        print(" ||        |")
        print(" ||        |")
        print(" ||")
        print(" ||")
        print(" ||")
        print(" ||")
        print("/()\\__")

    def hang_f():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||       (=)")
        print(" ||       /|\\")
        print(" ||      / | \\")
        print(" ||        |")
        print(" ||        |")
        print(" ||       /")
        print(" ||      /")
        print(" ||")
        print(" ||")
        print("/()\\__")

    def hang_g():
        print("")
        print("==============")
        print(">>> HANGER <<<")
        print("==============\n")
        print("/()\\")
        print(" ||=====><|||><")
        print(" ||        |")
        print(" ||       (=)")
        print(" ||       /|\\")
        print(" ||      / | \\")
        print(" ||        |")
        print(" ||        |")
        print(" ||       / \\")
        print(" ||      /   \\")
        print(" ||")
        print(" ||")
        print("/()\\__")

    if select == 1:
        hang_a()

    elif select == 2:
        hang_b()

    elif select == 3:
        hang_c()

    elif select == 4:
        hang_d()

    elif select == 5:
        hang_e()

    elif select == 6:
        hang_f()

    elif select == 7:
        hang_g()


# MAIN

# POSSIBLE ANSWERS
Yes = ["yes", "YES", "Yes", "yEs", "yeS", "YeS", "Y", "y", "yE", "ye", "YE", "Ye"]
No = ["No", "no", "NO", "nO", "N", "n"]

Valid = Yes + No
time.sleep(0.6)

print("\n========================")
print(">>> HANGING-MAN GAME <<<")
print("========================")

time.sleep(0.3)
user_input = input("\n>> Start the Game? (Yes or No): ")

# VALIDATION CHECKS FOR STARTING OR NOT
while user_input not in Valid:
    time.sleep(0.3)
    user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")

while user_input in Yes:
    time.sleep(0.3)
    word_file_loader()
    time.sleep(0.3)
    user_input = input("\n>> Start Again? (Yes or No): ")
    while user_input not in Valid:
        time.sleep(0.3)
        user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")
    if user_input in No:
        time.sleep(0.3)
        user_input = input("\n>> Confirm? (Yes or No): ")
        if user_input in Yes:
            break
        else:
            user_input = "Yes"

time.sleep(0.6)
print("\n=======================")
print(">>> ENDING THE GAME <<<")
print("=======================")
time.sleep(1.5)
