#! /usr/bin/env python
"""
TODO
"""

# imports go here

class Wordification:
    """" TODO """

    def __init__(self, string_representation, score):
        """ TODO """
        self.string_representation = string_representation
        self.score = score
        # this is really just an easier way of packaging a score with a wordification for manipulation later
        # the score is bonus
        # TODO I can probably rank the all_wordifications output by either score or alphabetical? That's a nice addition


class Wordification_Effort:
    """" TODO """
    def __init__(self, phone_number):
        """ TODO """
        self.phone_number = phone_number

        #TODO may just do this in main in the real thing, as I'm suspecting this class isn't worth the effort
        with open('scrabble_dict_2015.txt') as word_file:
            self.valid_words = set(word.strip().lower() for word in word_file)

        # Source for efficient check:
        # https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
        # Source for scrabble dictionary
        # https://boardgames.stackexchange.com/questions/38366/latest-collins-scrabble-words-list-in-text-file

        self.phone_dict = {
                            '2': ['a', 'b', 'c'],
                            '3': ['d', 'e', 'f'],
                            '4': ['g', 'h', 'i'],
                            '5': ['j', 'k', 'l'],
                            '6': ['m', 'n', 'o'],
                            '7': ['p', 'q', 'r', 's'],
                            '8': ['t', 'u', 'v'],
                            '9': ['w', 'x', 'y', 'z']
                          }

        self.reverse_phone_dict = {
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

    def number_to_words(self, provided_phone_number_string):
        """
            takes as an argument a string representing a US phone
            number and which outputs a string which has transformed part or all of the phone
            number into a single "wordified" phone number that can be typed on a US telephone
        """
        # get all the wordifications
        # step through them and find the highest scoring one
        # print that
        print("")
        return

    # TODO function to return the X top high scorers

    def words_to_number(self, wordification):
        """
            Outputs full-number version of a given wordification
        """
        output_string = ""
        # for character in string, just translate it. Should be trivial.
        for character in wordification:
            if character.lower() in self.reverse_phone_dict:
                output_string += self.reverse_phone_dict.get(character.lower())
            else:
                output_string += character
        print(output_string)
        return

    def all_wordifications(self):
        """
            Outputs all possible wordifications of a given number
        """
        for wordification in self.generate_all_wordifications():
            print(wordification.string_representation)
            # and probably, you know, some formatting stuff
        return

    def merge_and_concatenate_string_lists(self, list_of_lists_of_string_options):
        """
            Given a list of lists of strings, return a list of strings representing every possible result of picking
            exactly one string from each list and concatenating them
        """
        # TODO this method title kinda sucks right now
        # TODO input checking interpret any input as strings? (cast'em?)
        possible_resultant_strings = []

        # establish total number of combinations to check
        # make a list of indices for each list in the list of lists
        total_combinations = 1
        current_list_indices = []
        for list in list_of_lists_of_string_options:
            total_combinations *= len(list)
            # start em' all at zero
            current_list_indices.append(0)

        # TODO inelegant right now, but is there a cleaner way that's not way more convoluted?
        current_list_indices[0]=-1;

        for iteration in range(total_combinations):
            index_of_list_to_increment = 0;
            # increment the first one
            current_list_indices[index_of_list_to_increment] += 1;
            # if it hits its end, zero it and increment the next one (if that one hits it's end, ditto, etc.)
            while current_list_indices[index_of_list_to_increment] == len(list_of_lists_of_string_options[index_of_list_to_increment]):
                current_list_indices[index_of_list_to_increment] = 0
                index_of_list_to_increment += 1; #TODO go through and make sure I'm consistent with ++ vs +=1
                current_list_indices[index_of_list_to_increment] += 1;
                # wrap around
                if index_of_list_to_increment == len(current_list_indices):
                    index_of_list_to_increment = 0;
            # concatenate all those indices of those lists together
            result_string = ""
            for index in range(len(list_of_lists_of_string_options)):
                result_string += list_of_lists_of_string_options[index][current_list_indices[index]]
            possible_resultant_strings.append(result_string)

        return possible_resultant_strings

    def all_substring_groups(self, test_string):
        """
            Returns a list of all the possible subdivisions that can be made by slicing the provided string any
            number of times without changing its order.
        """
        # TODO make this static and useful for any string or...?
        # TODO substrings is a bad name here
        slice_group_list = []
        # do the operation on self.phone_number
        # (or on a given string, for versatility? maybe the class is more trouble than it's worth?)
        # cut paradigm
        # for all possible numbers of cuts (zero to one minus the number of characters in the string we're sub stringing)
        for valid_number_of_possible_cuts in range(len(test_string)):
            # create a list of cut indices with that # of entries
            current_cut_indices = []

            # initialize the cuts
            for cut in range(valid_number_of_possible_cuts):
                # the first relevant place is just after the first letter, and the rest are incremented from there
                current_cut_indices.append(cut + 1)

            # start with the last cut down the line and work back
            index_of_cut_to_move = len(current_cut_indices) - 1

            slicing_complete = False

            # the zero case. Easier to just spot-fix it than to get the slicing operation to work through empty lists.
            if valid_number_of_possible_cuts == 0:
                slicing_complete = True
                slice_group_list.append([test_string])

            # iterate through each slice, storing the resulting segments in the master list
            while not slicing_complete:
                # regroup which cut to move to the last most one
                index_of_cut_to_move = len(current_cut_indices) - 1
                # put together the start and end cut points with the current cut indices
                substring_values = [0]
                substring_values.extend(current_cut_indices)
                substring_values.append(len(test_string))
                # do the substring-ing
                slices_for_this_cut_group = []
                for index in range(len(substring_values) - 1):
                    slices_for_this_cut_group.append(test_string[substring_values[index]:substring_values[index + 1]])
                # save this subdivision group in the master list
                slice_group_list.append(slices_for_this_cut_group)

                # Check if the current cut can validly increment. If not, try the next cut up the line.
                # Also handle the stopping condition - if the earliest cut can't be incremented
                while not self.cut_advance_is_valid(current_cut_indices, index_of_cut_to_move, len(test_string)):
                    if index_of_cut_to_move == 0:
                        slicing_complete = True
                        break
                    else:
                        index_of_cut_to_move -= 1

                # increment (here so it always runs once)
                current_cut_indices[index_of_cut_to_move] += 1
                # regroup all the following cuts to be together in line after the moved cut
                for cut_number in range(len(current_cut_indices)):
                    if cut_number > index_of_cut_to_move:
                        current_cut_indices[cut_number] = current_cut_indices[cut_number - 1] + 1

        return slice_group_list

    def cut_advance_is_valid(self, current_cut_indices, index_of_cut_to_move, cut_string_length):
        """
            a helper function for all_substring_groups. Return boolean representing if advancing the provided
            cut to move would conflict with any existing cuts or with the limits of the string being cut, as
            determined by the provided group of cut indicies and the length of the cut string
        """
        potential_new_value = current_cut_indices[index_of_cut_to_move] + 1
        too_far = (potential_new_value == cut_string_length)
        conflicts_with_next_cut = False
        # checking the lastmost cut will give an index out of bounds, and it can't conflict with a later cut anyway.
        # So don't check it.
        if index_of_cut_to_move != (len(current_cut_indices) - 1):
            conflicts_with_next_cut = (potential_new_value == current_cut_indices[index_of_cut_to_move + 1])
        return not (too_far or conflicts_with_next_cut)

    def score_wordification(self, wordification, num_valid_translation_parts):
        """
        Return an ad-hoc score for a given wordification and number of parts used to make it. Allows for the easier
        selection of better quality wordifications by the user.
        Scoring rules are as follows:
        - golf score (lower is better)
        - each valid translation part is a point (discourage fragmentation)
        - each number before the first word is a point (discourage numbers)
        - each number after the first word is 1.5 points (numbers in the beginning are better than anywhere else)
        - for standard US 10 digit, if the first three are numbers, they don't count (everyone knows the area code)

        :param wordification: the string to score TODO do this for all of them
        :param num_valid_translation_parts: the number of pieces the given string was put together from
        :return: the score of the supplied wordification
        """
        score = 0
        first_word_begun = False
        nums_before_first_word_begun = 0
        for character in wordification:
            # if it's a letter
            if character in self.reverse_phone_dict:
                if not first_word_begun:
                    first_word_begun = True
            # if it's a number
            else:
                if first_word_begun:
                    score += 1.5
                else:
                    score += 1
                    nums_before_first_word_begun += 1
                    if nums_before_first_word_begun == 3 and len(wordification) == 10:
                        score -= 3
        score += num_valid_translation_parts

        return score

    def generate_all_wordifications(self, phone_number, best_x_to_save):
        """
            Returns a list of all possible wordifications of this effort's number
        """
        # a set, which is handy to check through and efficiently prevents repeat entries
        wordifications_list = set()
        best_scorers = []
        best_scores = []
        worst_score = None

        groups_to_check = self.all_substring_groups(phone_number)
        # for each group in groups_to_check
        for group in groups_to_check:
            valid_translation_parts = []
            # for each component of that group
            for component in group:
                # get a list of its valid *full* translations
                valid_translations = self.generate_valid_translations(component)
                # TODO valid translations should also include the full-number version of that chunk, but no all-full-number version (??)
                    # chunk object? word / number / score data members?
                    # maybe just leave the all-numbers in there, or filter it out at the end with an equality check?
                # store that list somewhere sensible
                valid_translation_parts.append(valid_translations)
            # add to the final list the every possible in-order concatenation of the valid translations parts
            for wordification in self.merge_and_concatenate_string_lists(valid_translation_parts):
                # don't add the original string, as it's not technically a wordification
                if wordification != phone_number:
                    wordifications_list.add(wordification)
                    # scoring
                    score = self.score_wordification(wordification, len(valid_translation_parts))
                    # keep the best x based on passed variable
                    if len(best_scorers) < best_x_to_save:
                        best_scorers.append(wordification)
                        best_scores.append(score)
                        if worst_score is None:
                            worst_score = score
                        elif score < worst_score:
                            worst_score = score
                    elif score < worst_score:
                        if wordification in best_scorers:
                            # find that wordification and replace its score
                            best_scores[best_scorers.index(wordification)] = score
                        else:
                            # find the worst wordification and replace its worst_score
                            best_scores[best_scores.index(worst_score)] = score
                            best_scorers[best_scores.index(worst_score)] = wordification
                        # update the worst score
                        worst_score = score

        return wordifications_list, best_scorers, best_scores

    def generate_valid_translations(self, number_string):
        """
            Input a string of numbers and return every possible valid full english translation of that string,
            plus the all-numbers variant
        """
        valid_translations = []
        valid_translations.append(number_string)

        letter_possibilities = []

        # for each number in number string
        for number in number_string:
            # translate it into a list of the letters it could be (lookup)
            # no english words contain internal blanks, so if you hit a zero or one you can comfortably skip the rest
            if number == '0' or number == '1':
                return valid_translations
            # input checking for safety, though it should never be relevant at this point
            elif number not in self.phone_dict:
                raise ValueError('Generate_valid_translations was asked to look up a non-number.')
            # if you hit a valid number, look up its translation
            else:
                letter_possibilities.append(self.phone_dict.get(number))

        # merge those lists with the list-merging method to get all the gibberish words it could be
        word_possibilities = self.merge_and_concatenate_string_lists(letter_possibilities)

        # if the word is a real word, add it to the valid translations list
        for word in word_possibilities:
            if self.check_if_valid_english_word(word):
                valid_translations.append(word)

        return valid_translations


    def check_if_valid_english_word(self, string_to_check):
        """ TODO """
        # check word against imported dictionary (?) in smart (??) and efficient (???) way
        # if it's valid return true, if not return false
        return string_to_check.lower() in self.valid_words




def main():
    """ nice UI and some tests probably """
    # greet
    # brief summary of wordifications
    # ask if they want to translate a wordification to a number or vice versa, or to exit
        # prompt for phone number
        # object to improper formatting, but allow it anyway on insistance
        # ask if they want the best, all of them, or exit to one level out, and supply the choice with the associated calls

    # TODO input checking for weird symbols, upper or lower, hyphens, etc.

    test_merge_and_concatenate = False
    test_all_substring_groups = False
    test_valid_words = False
    test_generate_valid_translations = False
    test_generate_all_wordifications = False
    test_words_to_number = True

    if test_merge_and_concatenate:
        test_effort = Wordification_Effort("401-867-5309")
        #list_of_lists_of_test_strings = [["I ","You ","We "],["like ","hate "],["vanilla.","chocolate.","strawberry."]]
        list_of_lists_of_test_strings = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
        resulting_strings = test_effort.merge_and_concatenate_string_lists(list_of_lists_of_test_strings)

        for index in range(len(resulting_strings)):
            print(str(index + 1) + ": " + resulting_strings[index])

    if test_all_substring_groups:
        test_effort = Wordification_Effort("401-867-5309")
        test_string = "horse"
        resulting_string_groups = test_effort.all_substring_groups(test_string)
        counter = 1
        print_str = ""
        for group in resulting_string_groups:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(group) + "\n"
        print(print_str)

    if test_valid_words:
        test_effort = Wordification_Effort("401-867-5309")
        test_string = "jinkies"
        result = test_effort.check_if_valid_english_word(test_string)
        print("Is \"" + test_string + "\" a valid English word? " + str(result))

    if test_generate_valid_translations:
        test_effort = Wordification_Effort("401-867-5309")
        test_string = "364"
        resulting_string_groups = test_effort.generate_valid_translations(test_string)
        counter = 1
        print_str = ""
        for group in resulting_string_groups:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(group) + "\n"
        print(print_str)

    if test_generate_all_wordifications:
        test_effort = Wordification_Effort("401-867-5309")
        test_string = "233"
        resulting_string_groups = test_effort.generate_all_wordifications(test_string)
        counter = 1
        print_str = ""
        for group in resulting_string_groups:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(group) + "\n"
        print(print_str)

    if test_words_to_number:
        test_effort = Wordification_Effort("401-867-5309")
        test_string = "877-CAs-HnoW"
        resulting_string_groups = test_effort.words_to_number(test_string)



# TODO make sure I'm not accidentally using any other built-in-function words as variable names (set, slice)

# TODO sanity check method to run all my wordifications back through my translator to check it

if __name__ == "__main__":
    main()

# TODO classes may need some reorganization; some of the methods are gonna be static otherwise, so probably don't include them in the class for clarity?
# TODO reorder methods so that ones that reference other ones come later