#! /usr/bin/env python
"""
TODO
"""

# state variable to allow the dictionary to only be loaded in once. I could avoid this by making the whole thing
# into a class and having this be a data member, but as and the original phone number are essentially the only shared
# pieces of information and most of the methods are static, I think this is cleaner.
valid_word_set = set()

def phone_dict_lookup(num_character):
    """
    :param num_character: a single number
    :return: a list of letters that correspond with that phone key. 0 and 1 are not represented.
    """
    phone_dict = {
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                 }
    # do this extra safely to avoid potential weird input issues
    return phone_dict.get(str(num_character).strip().lower(),None)

def reverse_phone_dict_lookup(letter_character):
    """
    :param letter_character: a single letter
    :return: the phone key that corresponds with that letter
    """
    reverse_phone_dict = {
                            'a': '2',
                            'b': '2',
                            'c': '2',
                            'd': '3',
                            'e': '3',
                            'f': '3',
                            'g': '4',
                            'h': '4',
                            'i': '4',
                            'j': '5',
                            'k': '5',
                            'l': '5',
                            'm': '6',
                            'n': '6',
                            'o': '6',
                            'p': '7',
                            'q': '7',
                            'r': '7',
                            's': '7',
                            't': '8',
                            'u': '8',
                            'v': '8',
                            'w': '9',
                            'x': '9',
                            'y': '9',
                            'z': '9'
                         }
    # do this extra safely to avoid potential weird input issues
    return reverse_phone_dict.get(str(letter_character).strip().lower(), None)

def check_if_valid_english_word(string_to_check):
    """
    Validate string against provided bank of words.
    :param string_to_check: string undergoing validation
    :param word_set: set of words considered valid
    :return: boolean indicating whether the provided string is represented in the valid set (True) or not (False)
    """
    return string_to_check.lower() in valid_word_set

def number_to_words(provided_phone_number_string):
    """
    As per project specifications, "Takes as an argument a string representing a US phone
    number and which outputs a string which has transformed part or all of the phone
    number into a single "wordified" phone number that can be typed on a US telephone"

    :param provided_phone_number_string: the phone number to wordify
    :return: Nothing. Simply outputs the result as per the project specifications.
    """
    all_answers, best_answer, best_score = generate_all_wordifications(provided_phone_number_string, 1)
    print(best_answer[0])
    return

def words_to_number(wordification):
    """
    As per project specifications, "Outputs full-number version of a given wordification"
    :param wordification: A string representing a phone number partially or fully replaced with words
    :return: Nothing. Simply outputs all results as per the project specifications.
    """
    output_string = ""
    # for character in string, translate it
    for character in wordification:
        translation = reverse_phone_dict_lookup(character)
        if translation is not None:
            output_string += translation
        else:
            output_string += character
    print(output_string)
    return

def possible_one_from_each_list_permutations(list_of_lists_of_string_options):
    """
    Return a list of strings representing every possible result of picking
    exactly one string from each of a given list of list of strings and concatenating them
    :param list_of_lists_of_string_options: a list of groups of strings,
                                            where one string from each group will be chosen per result
    :return: a list of all possible concatenated resultant strings
    """
    possible_resultant_strings = []

    # establish total number of permutations to check; make a list of indices for each list in the list of lists
    total_permutations = 1
    current_list_indices = []
    for list in list_of_lists_of_string_options:
        total_permutations *= len(list)
        # set each index at the beginning of its respective list
        current_list_indices.append(0)

    # set the first index back by one to account for the first increment, allowing for a more elegant loop
    current_list_indices[0] = -1;

    # execute once for each result
    for iteration in range(total_permutations):
        index_of_list_to_increment = 0;
        # increment the first one
        current_list_indices[index_of_list_to_increment] += 1;
        # if it hits its end, zero it and increment the next one (if that one hits its end, ditto, etc.)
        while current_list_indices[index_of_list_to_increment] == len(list_of_lists_of_string_options[index_of_list_to_increment]):
            current_list_indices[index_of_list_to_increment] = 0
            index_of_list_to_increment += 1
            current_list_indices[index_of_list_to_increment] += 1
        # concatenate all those indices of those lists together
        result_string = ""
        for index in range(len(list_of_lists_of_string_options)):
            result_string += str(list_of_lists_of_string_options[index][current_list_indices[index]])
        possible_resultant_strings.append(result_string)

    return possible_resultant_strings

def cut_advance_is_valid(current_cut_indices, index_of_cut_to_move, cut_string_length):
    """
    Return boolean representing if it would be permissible to increment the position of the provided cut, as defined
    by whether that incrementation would cause it to conflict with any other existing cuts or whether it cause the cut
    position to exeed the length of the string being cut.
    A helper function for all_possible_segmentations().
    :param current_cut_indices: Positions of all the current cuts in the string.
    :param index_of_cut_to_move: The index of the specific cut whose incrementation is being examined
    :param cut_string_length: The length of the string being cut
    :return: a boolean saying whether incrementing the position of the given cut is ok (True) or not (False)
    """
    potential_new_value = current_cut_indices[index_of_cut_to_move] + 1
    too_far = (potential_new_value == cut_string_length)
    conflicts_with_next_cut = False
    # checking the last-most cut will give an index out of bounds, and it can't conflict with a later cut anyway,
    # so don't check it
    if index_of_cut_to_move != (len(current_cut_indices) - 1):
        conflicts_with_next_cut = (potential_new_value == current_cut_indices[index_of_cut_to_move + 1])
    return not (too_far or conflicts_with_next_cut)

def all_possible_segmentations(string_to_segment):
    """
    Returns a list of all the possible subdivisions (themselves a list of all the pieces of a given subdivision)
    that can be made by slicing the provided string any number of times without changing its order.
    :param string_to_segment: the string to be subdivided
    :return: a list of each possible resulting list of segments
    """
    slice_group_list = []
    # cut paradigm - think of moving the spots in the string where you put the knife
    # for all possible numbers of cuts (zero to one minus the number of characters in the string we're sub-stringing)
    for valid_number_of_possible_cuts in range(len(string_to_segment)):

        # create a list of cut indices with that # of entries
        current_cut_indices = []

        # initialize the cuts
        for cut in range(valid_number_of_possible_cuts):
            # the first relevant place is just after the first letter, and the rest are incremented from there
            current_cut_indices.append(cut + 1)

        # start with the last cut down the line and work back
        index_of_cut_to_move = len(current_cut_indices) - 1

        # intialize stopping condition
        slicing_complete = False

        # the zero case. Easier to just spot-fix it than to get the slicing operation to work through empty lists.
        if valid_number_of_possible_cuts == 0:
            slicing_complete = True
            slice_group_list.append([string_to_segment])

        # iterate through each slice, storing the resulting segments in the master list, until no
        # no cut index can be incremented
        while not slicing_complete:
            # reset which cut to move to the last-most cut
            index_of_cut_to_move = len(current_cut_indices) - 1
            # put together the start and end cut points with the current cut indices
            substring_values = [0]
            substring_values.extend(current_cut_indices)
            substring_values.append(len(string_to_segment))
            # do the substring-ing
            slices_for_this_cut_group = []
            for index in range(len(substring_values) - 1):
                slices_for_this_cut_group.append(string_to_segment[substring_values[index]:substring_values[index + 1]])
            # save this subdivision group in the master list
            slice_group_list.append(slices_for_this_cut_group)

            # Check if the current cut-index can be validly incremented. If not, try the next cut up the line.
            # Also handle the stopping condition - if the earliest cut can't be incremented, the process is complete
            while not cut_advance_is_valid(current_cut_indices, index_of_cut_to_move, len(string_to_segment)):
                if index_of_cut_to_move == 0:
                    slicing_complete = True
                    break
                else:
                    index_of_cut_to_move -= 1

            # do the actual incrementation, now that a valid place has been found for it
            current_cut_indices[index_of_cut_to_move] += 1
            # regroup all the following cuts to be together in line after the moved cut
            for cut_number in range(len(current_cut_indices)):
                if cut_number > index_of_cut_to_move:
                    current_cut_indices[cut_number] = current_cut_indices[cut_number - 1] + 1

    return slice_group_list

def score_wordification(wordification, num_valid_translation_parts):
    """
    Return an ad-hoc score for a given wordification and number of parts used to make it. Allows for the easier
    selection of better quality wordifications by the user.
    Scoring rules are as follows:
    - golf score (lower is better)
    - each valid translation part is 10 points (discourage fragmentation)
      [ten points to avoid display issues with floats]
    - each number before the first word is 10 points (discourage numbers)
    - each number after the first word is 15 points (numbers in the beginning are better than anywhere else)
    - for standard US 10 digit, if the first three are numbers, they don't count (everyone knows the area code)
    - for standard US 11 digit if the first character is one and the first three after that are numbers, they
      also don't count (everyone knows to dial the one for long distance, and then the area code)

    :param wordification: the string to score
    :param num_valid_translation_parts: the number of pieces the given string was put together from
    :return: the score of the supplied wordification
    """
    score = 0
    first_word_begun = False
    first_character_is_one = wordification[0] == "1"
    nums_before_first_word_begun = 0
    for character in wordification:
        translation = reverse_phone_dict_lookup(character)
        # if it's a letter
        if translation is not None:
            if not first_word_begun:
                first_word_begun = True
        # if it's a number
        else:
            if first_word_begun:
                score += 15
            else:
                score += 10
                nums_before_first_word_begun += 1
                if nums_before_first_word_begun == 3 and len(wordification) == 10:
                    score -= 30
                elif nums_before_first_word_begun == 4 and len(wordification) == 11 and first_character_is_one:
                    score -= 40
    score += num_valid_translation_parts*10

    return score

def generate_valid_translations(number_string):
    """
    Input a string of numbers and return every possible valid full English translation of that string,
    plus the all-numbers variant.
    :param number_string: the string of numbers to fully translate (no partial translations)
    :return: the list of all full translations of the numbers into English words, plus the original all-number string
    """
    valid_translations = []

    # always include the full number version as a valid translation, as partial wordifications are acceptable.
    # requires filtering out the full-number translation, though.
    valid_translations.append(number_string)

    # place to store the lists of letters each number could be
    letter_possibilities = []

    # for each number provided...
    for number in number_string:
        # ...translate it into the list of the letters it could be
        lookup_result = phone_dict_lookup(number)
        # no english words contain internal blanks, so if you hit a zero or one you can comfortably skip this string
        if number == '0' or number == '1':
            return valid_translations
        # input checking for safety, though it should never be relevant at this point
        elif lookup_result is None:
            raise ValueError('Generate_valid_translations was asked to look up a non-number.')
        # if you hit a valid number, look up its translation
        else:
            letter_possibilities.append(lookup_result)

    # merge those lists with the list-merging method to get all the gibberish words it could be
    word_possibilities = possible_one_from_each_list_permutations(letter_possibilities)

    # if the word is a real word, add it to the valid translations list
    for word in word_possibilities:
        if check_if_valid_english_word(word):
            valid_translations.append(word)

    return valid_translations

def generate_all_wordifications(phone_number, best_x_to_save):
    """
    Returns a list of all possible wordifications of this effort's number
    :param phone_number: the phone number to attempt to wordify
    :param best_x_to_save: how many best-scorers the user wants to see
    :return: the list of all the wordifications, the list of all the best scorers, ad the list of all of
            the best scorer's scores
    """
    # a set, which is handy to check through and efficiently prevents repeat entries
    wordifications_list = set()

    # storage places for saving good scoring wordifications
    best_scorers = []
    best_scores = []
    worst_score = None

    # get all the possible subdivision groups of the original phone number
    groups_to_check = all_possible_segmentations(phone_number)

    # for each of those subdivision groups...
    for group in groups_to_check:
        valid_translation_parts = []
        # for each subdivided chunk...
        for component in group:
            # get a list of that chunk's valid *full* translations and add it to the larger list of valid options
            valid_translation_parts.append(generate_valid_translations(component))
        # add possible in-order concatenation of the valid translations parts to the final list
        for wordification in possible_one_from_each_list_permutations(valid_translation_parts):
            # don't add the original string, as it's not technically a wordification
            if wordification != phone_number:
                wordifications_list.add(wordification)
                # Do some scoring - a bonus feature made to help the user find better wordifications
                # scoring has to be done here, otherwise information about the number of words (AKA the number of valid
                # translation parts) will be lost, and it's painful to recover.
                score = score_wordification(wordification, len(valid_translation_parts))
                # keep the best x wordifications based on the passed variable
                # if there are no recorded members yet, initialize the worst_score and add the first-comer to the list
                if worst_score is None:
                    worst_score = score
                    best_scorers.append(wordification)
                    best_scores.append(score)
                # if the best x wordifications haven't been found yet, add it to the list
                elif len(best_scorers) < best_x_to_save:
                    # no repeats! if you're already represented somehow...
                    if wordification in best_scorers:
                        # find the copy and replace its score
                        best_scores[best_scorers.index(wordification)] = score
                    # otherwise just add yourself to the list
                    else:
                        best_scorers.append(wordification)
                        best_scores.append(score)
                    # update the worst score, if relevant
                    if score < worst_score:
                        worst_score = score
                # if the top X have already been found, but you're better than the worst of them, you need to find
                # who you can replace
                elif score < worst_score:
                    # no repeats! if you're already represented somehow...
                    if wordification in best_scorers:
                        # find the copy and replace its score
                        best_scores[best_scorers.index(wordification)] = score
                    # otherwise find the worst wordification in the list and replace its worst_score
                    else:
                        best_scores[best_scores.index(worst_score)] = score
                        best_scorers[best_scores.index(worst_score)] = wordification
                    # update the worst score
                    worst_score = score
    # return all three lists for outside use
    return wordifications_list, best_scorers, best_scores

def all_wordifications(given_number):
    """
    As per project specifications, "Outputs all possible wordifications of a given number"
    :param given_number: a user-specified number
    :return: nothing, simply outputs as per specifications
    """
    for wordification in generate_all_wordifications(given_number):
        print(wordification)
    return

def run_various_tests():
    """
    A function to hold various test cases. Used in debugging and left in for posterity.
    :return: Nothing
    """
    test_possible_one_from_each_list_permutations = False
    test_all_possible_segmentations = False
    test_valid_words = False
    test_generate_valid_translations = False
    test_generate_all_wordifications = False
    test_words_to_number = False
    test_score_wordification = True

    if test_possible_one_from_each_list_permutations:
        #list_of_lists_of_test_strings = [["I ","You ","We "],["like ","hate "],["vanilla.","chocolate.","strawberry."]]
        list_of_lists_of_test_strings = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                                        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
        resulting_strings = possible_one_from_each_list_permutations(list_of_lists_of_test_strings)

        for index in range(len(resulting_strings)):
            print(str(index + 1) + ": " + resulting_strings[index])

    if test_all_possible_segmentations:
        test_string = "horse"
        resulting_string_groups = all_possible_segmentations(test_string)
        counter = 1
        print_str = ""
        for group in resulting_string_groups:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(group) + "\n"
        print(print_str)

    if test_valid_words:
        test_string = "jinkies"
        result = check_if_valid_english_word(test_string)
        print("Is \"" + test_string + "\" a valid English word? " + str(result))

    if test_generate_valid_translations:
        test_string = "364"
        resulting_string_groups = generate_valid_translations(test_string)
        counter = 1
        print_str = ""
        for group in resulting_string_groups:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(group) + "\n"
        print(print_str)

    if test_generate_all_wordifications:
        test_string = "233"
        resulting_string_groups = generate_all_wordifications(test_string)
        counter = 1
        print_str = ""
        for group in resulting_string_groups:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(group) + "\n"
        print(print_str)

    if test_words_to_number:
        test_string = "877-CAs-HnoW"
        resulting_string_groups = words_to_number(test_string)

    if test_score_wordification:
        print(score_wordification("1111erta456",3))

def main():
    """ nice UI and some tests probably """
    # greet
    # brief summary of wordifications
    # ask if they want to translate a wordification to a number or vice versa, or to exit
        # prompt for phone number
        # object to improper formatting, but allow it anyway on insistance
        # ask if they want the best, all of them, or exit to one level out, and supply the choice with the associated calls

   # TODO run input checking in a method and put it on all of the stock given methods, because they probably test using those 

    with open('scrabble_dict_2015.txt') as word_file:
        valid_word_set = set(word.strip().lower() for word in word_file)

    # Source for efficient check:
    # https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
    # Source for scrabble dictionary
    # https://boardgames.stackexchange.com/questions/38366/latest-collins-scrabble-words-list-in-text-file



    run_various_tests()



    # TODO input checking for weird symbols, upper or lower, hyphens, etc.

# TODO sanity check method to run all my wordifications back through my translator to check it

if __name__ == "__main__":
    main()

