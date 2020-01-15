# Asks user to submit words for a Michael Bay themed madlib,
# then returns the completed madlib

#installs
import sys

def create_madlib():
    # Blank madlib
    blank_madlib = """
    __(mans_name)__ is a normal __(occupation)__. Then, one day, a __(noun)__ 
    explodes, causing a __(noun)__ to blow up, and a nearby __(noun)__ 
    erupts into a __(shape)__ of flames. __(mans_name)__ realizes that he's 
    being chased by the government, who's trying to __(verb)__ him. While on 
    the run, he teams up with a woman named __(womans_name)__.  The duo decide 
    to turn the tables on their pursuers by blowing up a __(noun)__, which 
    triggers a chain reaction, causing the local __(noun)__, __(restaurant)__ 
    and the __(historic_monument)__ to explode. Then, the bad guys' helicopter 
    gets __(verb)__ed by a piece of __(noun)__ from when the __(noun)__ 
    exploded, and the helicopter explodes falling onto a __(noun)__, 
    causing it to __(verb)__ and destroy the bad guys. Everything is 
    __(adjective)__ and the two decide that such a __(adjective)__ ordeal 
    has caused them to fall in __(emotion)__ with each other. They decide to 
    celebrate by __(verb)__ing on the __(noun)__, and they even managed to 
    use a __(noun)__ from the beginning of the movie, to __(verb)__ the 
    whole story together.
    """

    # Assign madlib words
    
    mans_name, womans_name = "", ""
    occupation, emotion, shape = "", "", ""
    restaurant, historic_monument = "", ""
    noun1, noun2, noun3, noun4, noun5 =  "", "", "", "", ""
    noun6, noun7, noun8, noun9 = "", "", "", ""
    verb1, verb2, verb3, verb4, verb5 = "", "", "", "", ""
    adjective1, adjective2 = "", ""

    word_list = ["mans_name", "womans_name", "occupation", "emotion", "shape",
    "restaurant", "historic_monument", "noun1", "noun2", "noun3", "noun4",
    "noun5", "noun6", "noun7", "noun8", "noun9", "verb1", "verb2", "verb3", 
    "verb4", "verb5", "adjective1", "adjective2"]

    user_input_list = []

    print("\nPlease help us complete the below madlib by submitting words!\n", 
    blank_madlib)

    for word in word_list:
        
        user_input = ""

        while user_input == "":
            user_input = input("Please input " + word +":\n")

        if user_input == "exit()" or user_input == "exit" or user_input == "cancel":
            sys.exit("Cancelling program...")

        user_input_list.append(user_input)
        print("\n")

    mans_name, womans_name, occupation, emotion, shape, restaurant, historic_monument, noun1, noun2, noun3, noun4, noun5, noun6, noun7, noun8, noun9, verb1, verb2, verb3, verb4, verb5, adjective1, adjective2 = user_input_list

    # Madlib readout
    completed_madlib = """
    __{mans_name}__ is a normal __{occupation}__. Then, one day, a __{noun1}__ 
    explodes, causing a __{noun2}__ to blow up, and a nearby __{noun3}__ 
    erupts into a __{shape}__ of flames. __{mans_name}__ realizes that he's 
    being chased by the government, who's trying to __{verb1}__ him. While on 
    the run, he teams up with a woman named __{womans_name}__.  The duo decide 
    to turn the tables on their pursuers by blowing up a __{noun4}__, which 
    triggers a chain reaction, causing the local __{noun5}__, __{restaurant}__ 
    and the __{historic_monument}__ to explode. Then, the bad guys' helicopter 
    gets __{verb2}__ed by a piece of __{noun6}__ from when the __{noun4}__ 
    exploded, and the helicopter explodes and falls onto a __{noun7}__, 
    causing it to __{verb3}__ destroying the bad guy leader. Everything is 
    __{adjective1}__ and the two decide that such a __{adjective2}__ ordeal 
    has caused them to fall in __{emotion}__ with each other. They decide to 
    celebrate by __{verb4}__ing on the __{noun8}__, and they even managed to 
    use a __{noun9}__ from the beginning of the movie, to __{verb5}__ the 
    whole story together.
    """.format(mans_name=mans_name, womans_name=womans_name, 
    occupation=occupation, emotion=emotion, shape=shape,
    restaurant=restaurant, historic_monument=historic_monument, 
    noun1=noun1, noun2=noun2, noun3=noun3, noun4=noun4, noun5=noun5,
    noun6=noun6, noun7=noun7, noun8=noun8, noun9=noun9,
    verb1=verb1, verb2=verb2, verb3=verb3, verb4=verb4, verb5=verb5,
    adjective1=adjective1, adjective2=adjective2)

    print("Here is the madlib!\n", completed_madlib)

create_madlib()