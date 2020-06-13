# coding: utf-8
import string
import random


"""
Hard-Coded List of Strings
Many of them are from A3
"""

# These will be used for my Chatbot, Ericus.

QUESTION_LIST = ["How are you doing?", "How old are you?", "What's up?",
                 "What's your favorite color?", "Want to be buddies?"]

WAYS_TO_SAY_YES = ["yes", "sure", "why not", "ok", "okay",
                   "alright", "all right", "for sure", "yeah", "yep",
                   "yea", "ya", "ye", "yup", "yesss", "yasss"]

WAYS_TO_SAY_NO = ["no", "nah", "no thanks", "not today",
                  "I'll pass", "nein", "never", "i'm ok"]

GREETINGS_IN = ["hello", "hi", "hey", "hola",
                "welcome", "bonjour", "greetings"]

GREETINGS_OUT = ["Hello, it's nice to talk to you!",
                 "Nice to meet you!", "Hey - Let's chat!"]

COMP_IN = ["python", "code", "computer", "algorithm", ]

COMP_OUT = ["Python is what I'm made of.", "Did you know I'm made of code!?",
            "Computers are so magical",
            "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ["turing", "hopper", "neumann", "lovelace"]

PEOPLE_OUT = ["was awesome!", "did so many important things!",
              "is someone you should look up :)."]

PEOPLE_NAMES = {"turing": "Alan", "hopper": "Grace",
                "neumann": '"John" von', "lovelace": 'Ada'}

JOKES_IN = ["funny", "hilarious", "ha", "haha", "hahaha", "lol"]

JOKES_OUT = ["ha", "haha", "lol"]

NONO_IN = ["matlab", "java", "C++"]

NONO_OUT = ["I'm sorry, I don't want to talk about"]

UNKNOWN = ["Good.", "Okay", "Huh? Ok then I guess.",
           "Huh, that's pretty interesting!", "Cool.", "Yeah!", "Thanks!",
           "Awesome!"]

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"


def is_question(input_string):
    """
    Given the input to the chatbot, determine if it is a question.

    :param input_string: string
    :return: boolean

    """

    # Checking if there is a question mark in the string using 'in'
    if "?" in input_string:
        output = True

    # If there is no question mark, return False
    else:
        output = False

    return output


def remove_punctuation(input_string):
    """
    Gets rid of all punctuation in a string.

    :param input_string: string
    :return: string

    """

    # Goes through every element in the input,
    out_string = ""
    for i in input_string:

        # If the element is not a punctuation,
        # then append it into output string
        if i not in string.punctuation:
            out_string = out_string + i

    return out_string


def prepare_text(input_string):
    """
    Makes string lowercase, removes all punctuation, then
    splits the string into words.

    :param input_string: string
    :return: list of strings

    """

    # Makes the input lowercase, then uses our
    # previous function to remove punctuation marks
    temp_string = remove_punctuation(input_string.lower())

    # This will split the string into a list of words
    out_list = temp_string.split()

    return out_list


def respond_echo(input_string, number_of_echoes, spacer):
    """
    Return a string that has been repeated a specified number
    of times, with a given separator.

    :param input_string: string or None
    :param number_of_echoes: integer
    :param spacer: string
    :return: string or None

    """

    echo_output = ""

    # As long as input has some value,
    # Sets echo_output to be the combination of input
    # and spacer a set multiple of times
    if input_string is not None:
        echo_output = (input_string + spacer) * number_of_echoes

    # If there is no input_string value, there is no echo_output value
    elif input_string is None:
        echo_output = None

    return echo_output


def selector(input_list, check_list, return_list):
    """
    Take a list of words that we got as input,
    a list of words to check for whether they appear in the input,
    and a list of possible outputs to return if something
    from the list to check is in the input list.

    :param input_list: list of strings
    :param check_list: list of strings
    :param return_list: list of strings
    :return: string or None

    """

    # Goes through every element in a list,
    output = None
    for i in input_list:

        # If that element is in a second list,
        # then a random element of a third list is outputted
        if i in check_list:
            output = random.choice(return_list)
            break

    return output


def string_concatenator(string1, string2, separator):
    """
    Concatenate two strings, combining them with a specified separator.

    :param string1: string
    :param string2: string
    :param separator: string
    :return: string

    """

    # The first two inputs are combined, with the third input in between them
    output = string1 + separator + string2

    return output


def list_to_string(input_list, separator):
    """
    Turn a list of strings back into one single concatenated string.
    Return a string that is each element of input_list concatenated together
    with each other separated by the string separator.

    :param input_list: list of strings
    :param separator: string
    :return: string

    """

    # Takes the first element of an input list,
    # then goes through the other elements of that list and
    output = input_list[0]

    # combines it to the first element, with an input separator in between
    # each element.
    for i in input_list[1:]:
        output = output + separator + i

    return output


def end_chat(input_list):
    """
    End the chatbot conversation if the word 'quit' shows up.

    :param input_list: list
    :return: boolean

    """

    # If the word 'quit' shows up in the inputted list, then True
    if "quit" in input_list:
        output = True

    # If 'quit' isn't there, then False
    else:
        output = False

    return output


def is_in_list(list_one, list_two):
    """
    Check if any element of list_one is in list_two.

    :param list_one: list
    :param list_two: list
    :return: boolean

    """

    # Goes through every element in input list
    for element in list_one:

        # If the element is also in a second list, then True
        if element in list_two:
            return True

    return False


def find_in_list(list_one, list_two):
    """
    Find and return an element from list_one that is in list_two,
     or None otherwise.

    :param list_one: list
    :param list_two: list
    :return: item in list

    """

    # Goes through every element in a list
    for element in list_one:

        # If the element is also in the second list, then print it out
        if element in list_two:
            return element

    return None


def get_name():
    """
    Asks the person for their name as the input.

    :return: string

    """

    # Asks for the human to input his/her name
    msg = input("Hi, what's your name? \n")
    # Responds using the human's input to create a string introducing Ericus.
    out_msg = "Hi "+ msg + " my name is Ericus!"

    print(out_msg)


def play_game():
    """
    After answering 'yes' or 'no' to playing a game,
    Ericus asks the person what game he/she would like to play.

    :return: N/A

    """

    # choose from coin flip, rock paper scissors, or guess a number
    new_game = input("ERICUS: What game? Please enter a Number "
                         " 1. Rock-Paper-Scissors 2. Coin Flip "
                         "3. Pick a Number\n")

    # If the human enters 1, the function to play Rock-Paper-Scissors runs
    if new_game == "1":
            rock_paper_scissors()

    # If the human enters 2, the function to play coin flip runs
    elif new_game == "2":
            coin_flip()

    # If the human enters 3, the function to play pick a number runs
    elif new_game == "3":
            pick_number()


def rock_paper_scissors():
    """
    The human selects either 'rock', 'paper', or 'scissors',
    against Ericus' random selection.

    :return: String

    """

    # Prompts human to choose 'rock', 'paper', or 'scissors'
    choices = ["rock", "paper", "scissors"]
    human_guess = input("ERICUS: Your choices are rock, paper, "
                        "or scissors. What do you choose?\n")
    # This chooses the computer's selection at random
    comp_guess = random.choice(choices)


    if human_guess == "rock" and comp_guess == "rock":
        print("ERICUS: I chose rock, too. Looks like we tied.")

    if human_guess == "rock" and comp_guess == "paper":
        print("ERICUS: I chose paper. I win haha.")

    if human_guess == "rock" and comp_guess == "scissors":
        print("ERICUS: You won, I picked scissors.")

    if human_guess == "paper" and comp_guess == "rock":
        print("ERICUS: You won, I picked rock.")

    if human_guess == "paper" and comp_guess == "paper":
        print("ERICUS: I chose paper, too. Looks like we tied.")

    if human_guess == "paper" and comp_guess == "scissors":
        print("ERICUS: I chose scissors. I win haha.")

    if human_guess == "scissors" and comp_guess == "scissors":
        print("ERICUS: I chose scissors, too. Looks like we tied.")

    if human_guess == "scissors" and comp_guess == "rock":
        print("ERICUS: I chose rock. I win haha.")

    if human_guess == "scissors" and comp_guess == "paper":
        print("ERICUS: You won, I picked paper.")

    # This gives the human the option to play  rock paper scissors again
    replay_mini_game = input("Play again? \n")

    # If their response is in the list WAYS_TO_SAY_YES
    # then the function runs again
    if replay_mini_game in WAYS_TO_SAY_YES:
        rock_paper_scissors()

    # If their response is in the list WAYS_TO_SAY_NO
    # then the replay() function runs
    elif replay_mini_game in WAYS_TO_SAY_NO:
        replay()


def coin_flip():
    """
    The human selects 'heads' or 'tails'
    when Ericus flips a coin.

    :return: String

    """

    # The human chooses from choices and the flip is a
    # random choice from choices
    choices = ["heads", "tails"]
    human_guess = input("ERICUS: So heads or tails?\n")
    the_flip = random.choice(choices)

    if the_flip == "heads":
        print("ERICUS: Heads like the lettuce.")

    else:
        print("ERICUS: It's tails.")

    # This gives the option to play coin flip
    replay_mini_game = input("Play again? \n")

    # If their response is in the list WAYS_TO_SAY_YES
    # then the function runs again
    if replay_mini_game in WAYS_TO_SAY_YES:
        coin_flip()

    # If their response is in the list WAYS_TO_SAY_NO then
    # the replay() function runs
    elif replay_mini_game in WAYS_TO_SAY_NO:
        replay()


def pick_number():
    """
    The human tries to guess what Ericus' number is between 1 to 20

    :return: String

    """

    # Human selects number between 1 and 20, which is
    # expressed by the range method
    # The number is selected by using the random.choice method for choices
    choices = range(1, 20)
    human_guess = int(input("ERICUS: Guess a number between 1 and 20. "
                            "I'll tell you a secret if you guess correctly!"
                            "\n"))
    number = random.choice(choices)

    if human_guess == number:
        print("ERICUS: WOW. You got it! It was indeed " + str(number) +
              ". My secret is that my name is actually Eric.")

    else:
        print("ERICUS: Way off! The number was " + str(number))

    # This gives the option to play pick a number again
    replay_mini_game = input("Play again? \n")

    # If their response is in the list WAYS_TO_SAY_YES
    # then the function runs again
    if replay_mini_game in WAYS_TO_SAY_YES:
        pick_number()

    # If their response is in the list WAYS_TO_SAY_NO
    # then the replay() function runs
    elif replay_mini_game in WAYS_TO_SAY_NO:
        replay()


def replay():
    """
    This function is for when the human wants
    to stop playing the current game, or wants to
    play a different game

    :return: String

    """

    # Gives human the option to play another game
    decision = input("ERICUS: Do you want to play a different game? \n")

    # If the user says one of the items in WAYS_TO_SAY_YES,
    if decision in WAYS_TO_SAY_YES:
        # Ericus will ask what games the person can select from
        new_game = input("ERICUS: What game? Please enter a Number "
              " 1. Rock-Paper-Scissors 2. Coin Flip "
                         "or 3. Pick a Number\n")

        if new_game == "1":
            rock_paper_scissors()

        elif new_game == "2":
            coin_flip()

        elif new_game == "3":
            pick_number()

    # If the person does not say yes, then Ericus will
    # stop playing games and start chatting
    else:
        print("ERICUS: Alrighty then.")


def pick_question():
    """
    Chooses a question at random to ask the person.

    :return: space for person's input.

    """

    # Chooses a random item from question list and assigns it to a variable
    question = random.choice(QUESTION_LIST)

    # After the item is selected, it is removed from the question list
    QUESTION_LIST.remove(question)

    return input(question + "\n")


def lets_chat():
    """
    Main function to run our chatbot.
    Half of this code is from A3 Chatbots, part 4.

    :return: String

    """

    # The first thing Ericus does is ask the person for their name
    get_name()

    # Ericus then asks if the person wants to play a game
    # If the response is in WAYS_TO_SAY_YES, then run the play game function
    if (input("Do you wanna play a game? \n") in WAYS_TO_SAY_YES):
        play_game()

    chat = True
    while chat:

        # Get a message from the user
        if len(QUESTION_LIST) == 0:
            msg = input("Say somthing: \t")

        else:
            msg = pick_question()

        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg
        if end_chat(msg):
            out_msg = "Bye!"
            chat = False

        # Check for a selection of topics that we have defined to respond to
        # Here, we will check for a series of topics that
        # we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting,
            # add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing,
            # add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified,
            # add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name],
                                            name.capitalize(),
                                            selector(msg, PEOPLE_IN,
                                                     PEOPLE_OUT)], " "))

            # Check if the input looks like a joke,
            # add a repeat joke output if so
            outs.append(respond_echo(selector(msg,
                                              JOKES_IN, JOKES_OUT), 3, ""))

            # Check if the input has some words we don't
            # want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT),
                                            find_in_list(msg, NONO_IN)], " "))

            # We could have selected multiple outputs from the
            # topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases,
            #   meaning we don't have a reply
            #   To deal with this, we are going to randomly select
            #   an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question,
        # return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print("ERICUS:", out_msg)