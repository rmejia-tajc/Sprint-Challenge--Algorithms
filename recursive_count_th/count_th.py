'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # check to see if "th" is in word. If false, it will return -1, otherwise it will return the index of the first find
    place = word.find("th")
    # if "th" is not found...
    if place == -1:
        return 0
    # if "th" is found...
    else:
        # create a new word omitting the current found "th" by moving the index 2 spaces to the right and starting the new word from that index
        new_word = word[ place + 2: ]
        # count the current "th" as one and add anyothers found by running count_th again on new_word
        number = 1 + count_th(new_word)

        # return the total number of occurrences of "th"
        return number