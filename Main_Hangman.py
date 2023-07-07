# IMPORTED LIBRARIES:
import random
import time

# FUNCTIONS:
def word_file_loader(): #LOADS WORDS FROM FILE

    # CHECKS IF FILE EXISTS OR NOT
    try:
        file = open("Wordlist.txt", "r")
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
    read_file_line = file.readline()

    # READING A FILE IF IT IS NOT EMPTY
    if read_file_line == "":
        time.sleep(0.7)
        print("\n==========================")
        print(">>> WORD FILE IS EMPTY <<<")
        print("==========================")
        print("\n>> Please Fill 'Wordlist.txt' to Continue...")
        file.close()

    else:
        wordlist = []

        # LOADS WORDLIST FROM FILE
        while True:
            wordlist.append(str(read_file_line))
            read_file_line = str(file.readline())
            if read_file_line == "":
                break

        # SELECTS RANDOM WORD FROM THE WORDLIST
        selected_word = random.choice(wordlist)
        file.close()
        main_game(selected_word)

def main_game(selected_word): #MANAGES THE GAME

    word_length = len(selected_word)

    # DECIDES THE NUMBER OF HIDDEN WORDS
    if word_length <= 4:
        hidden_counts = 2
    elif word_length > 4 and (word_length <= 6):
        hidden_counts = 3
    elif word_length > 6 and (word_length <= 8):
        hidden_counts = 4
    elif word_length > 8 and (word_length <= 10):
        hidden_counts = 6
    elif word_length > 10 and (word_length <= 12):
        hidden_counts = 7
    elif word_length > 12 and (word_length <= 14):
        hidden_counts = 9
    elif word_length > 14 and (word_length <= 16):
        hidden_counts = 11
    elif word_length > 16 and (word_length <= 18):
        hidden_counts = 13
    else:
        hidden_counts = 15

    # DECIDES WHICH INDEX OF THE WORD TO HIDE
    hidden_index = random.sample(range(0, word_length), hidden_counts)
    hidden_index.sort()

    # ELIMINATING "SPACES" FROM THE INDEX LIST
    for index in range(word_length):
        if (selected_word[index] == " " or (selected_word[index] == "\n")) and (index in hidden_index):
            hidden_index.remove(index)

    # CHARACTER LIST FOR HIDDEN
    hidden_charlist_upper = []
    hidden_charlist_lower = []

    for index in range(word_length):
        if index in hidden_index:
            hidden_charlist_upper.append(selected_word[index].upper())
            hidden_charlist_lower.append(selected_word[index].lower())

    character_left = len(hidden_index)

    # GENERATING A CIPHERED STRING
    generated_string = ""

    for index in range(word_length):
        if index in hidden_index:
            generated_string += "_"
        else:
            generated_string += selected_word[index]

    # STRING DISPLAY
    print("\n======================")
    print(">>> GUESS THE WORD <<<")
    print("======================")
    time.sleep(0.3)
    print("\n>> WORD: " + generated_string)

    # INPUT FROM USER, IN CASE OF WORD IT ONLY TAKES FIRST CHARACTER
    Won = False
    attempts = 1

    while True:
        user_input = input(">> Enter Your Guess: ")
        while user_input == "":
            user_input = input(">> Invalid Input!: ")
        user_input = user_input[0]

        # CHECKING THE VALUES
        if user_input.upper() in hidden_charlist_upper:
            time.sleep(0.6)
            print("\n=====================")
            print(">>> CORRECT GUESS <<<")
            print("=====================")

            # REMOVE THE CHARACTER AND ITS INDEX FROM HIDDEN LIST
            while user_input.upper() in hidden_charlist_upper:
                temp = hidden_charlist_upper.index(user_input.upper())
                temp_a = hidden_index[temp]
                hidden_charlist_lower.remove(user_input.lower())
                hidden_charlist_upper.remove(user_input.upper())
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
                Won = True
                break
        else:
            time.sleep(0.5)
            Graphics(attempts)
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

    # WINNING SITUATIONS
    if Won:
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

def Graphics(Select): #HANGINGMAN ANIMATIONS/GRAPHICS

    def Hang_A():
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

    def Hang_B():
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

    def Hang_C():
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

    def Hang_D():
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

    def Hang_E():
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

    def Hang_F():
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

    def Hang_G():
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

    if Select == 1:
        Hang_A()

    elif Select == 2:
        Hang_B()

    elif Select == 3:
        Hang_C()

    elif Select == 4:
        Hang_D()

    elif Select == 5:
        Hang_E()

    elif Select == 6:
        Hang_F()

    elif Select == 7:
        Hang_G()

#MAIN SCREEN:

#POSSIBLE ANSWERS
Yes = ["yes", "YES", "Yes", "yEs", "yeS", "YeS", "Y", "y", "yE", "ye", "YE", "Ye"]
No = ["No", "no", "NO", "nO", "N", "n"]

Valid = Yes + No
time.sleep(0.6)

print("\n=======================")
print(">>> HANING MAN GAME <<<")
print("=======================")

time.sleep(0.3)
user_input = input("\n>> Start the Game? (Yes or No): ")

# VALIDATION CHECKS FOR STARTING OR NOT
while user_input not in Valid:
    time.sleep(0.3)
    user_input = input(">> Invalid Input! (Yes or No): ")

while user_input in Yes:
    time.sleep(0.3)
    word_file_loader()
    time.sleep(0.3)
    user_input = input("\n>> Start Again? (Yes or No): ")
    if user_input in No:
        time.sleep(0.3)
        user_input = input("\n>> Confirm? (Yes or No): ")
        if user_input in Yes:
            user_input = "No"

time.sleep(0.6)
print("\n=======================")
print(">>> ENDING THE GAME <<<")
print("=======================")
time.sleep(1.5)
