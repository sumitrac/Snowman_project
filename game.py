from wonderwords import RandomWord

SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
MAX_WRONG_GUESSES = 7
SNOWMAN_MAX_WRONG_GUESSES = 7


SNOWMAN_1 = '\n *   *   *'
SNOWMAN_2 = '   * _ *   '
SNOWMAN_3 = '    [_]    '
SNOWMAN_4 = '   /(")\   '
SNOWMAN_5 = ' *_( : )_* '
SNOWMAN_6 = '  (_ : _)  '
SNOWMAN_7 = '-----------\n'

r = RandomWord()
snowman_word = r.word(
  word_min_length = SNOWMAN_MIN_WORD_LENGTH, word_max_length = SNOWMAN_MAX_WORD_LENGTH
  )


def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratuations, you win!'
    If the player wins and, 'Sorry, you lose!  The word was {snowman_word}' if the player loses
    """
    
    #assigning variable 
    list_of_letters = build_word_list(snowman_word)
    #empty list to hold correct & wrong guesses  
    correct_guesses_list = []
    wrong_list = []
    #This section sets game at zero 
    corrects_counter = 0
    num_wrong_guesses = 0
    

    while len(wrong_list) < SNOWMAN_MAX_WRONG_GUESSES: 
      user_input = get_letter_from_user(correct_guesses_list, wrong_list)
      all_letters_guessed = update_and_check_word_list(list_of_letters, user_input)
      
      #this section prints the messages: win, correct or wrong guesses
      if all_letters_guessed:
        print("Congratulations, you win!")
        break
      elif user_input in snowman_word:
        print("You guessed a letter that's in the word!")
        correct_guesses_list.append(user_input) 
        corrects_counter += 1
      else:
        print(f"The letter {user_input} is not in the word")
        wrong_list.append(user_input) 
        num_wrong_guesses += 1

      print_snowman_graphic(len(wrong_list))
      print_word_list(list_of_letters)
      print("Wrong guesses: " + " ".join(wrong_list))
      print(f"You have made {corrects_counter} correct and {num_wrong_guesses} incorrect guesses\n")
    
    #this section prints losing message
    if num_wrong_guesses == SNOWMAN_MAX_WRONG_GUESSES:
        print(f"Sorry, you lose!  The word was {snowman_word}")


def print_snowman_graphic(num_wrong_guesses):
    """This function prints a portion of the 
    snowman depending on the number of 
    wrong guesses
    """
    
    for i in range(1, num_wrong_guesses + 1):
        if(i == 1):
            print(SNOWMAN_1)
        if(i == 2):
            print(SNOWMAN_2)
        if(i == 3):
            print(SNOWMAN_3)
        if(i == 4):
            print(SNOWMAN_4)
        if(i == 5):
            print(SNOWMAN_5)
        if(i == 6):
            print(SNOWMAN_6)
        if(i == 7):
            print(SNOWMAN_7)


def build_word_list(word):
    """This function builds a list of dictionaries
    With each letter and "guessed": False
    Example: [ { 'letter': 'a', 'guessed': False }, 'letter': 'b', 'guessed': False }, ]
    """
    word_list = []
    for letter in word:
        letter_dict = {"letter": letter, "guessed": False}
        word_list.append(letter_dict)
    return word_list


def print_word_list(word_list):
    """This function prints the letters of the word
    based on if that letter has been guessed or not
    """

    output_string = ""
    for elem in word_list:
        if elem["guessed"]:
            output_string += elem["letter"]
        else:
            output_string += "_"
        output_string += " "
    print(output_string)


def get_letter_from_user(wrong_list, correct_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string


def update_and_check_word_list(list_of_letters, guessed_letter):
    all_letters_guessed = True
    for letter_dict in list_of_letters:
        if (guessed_letter == letter_dict["letter"]):
            letter_dict["guessed"] = True
        elif (not letter_dict["guessed"]):
            all_letters_guessed = False
    
    return all_letters_guessed
