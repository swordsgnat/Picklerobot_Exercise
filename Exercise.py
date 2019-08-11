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

    def words_to_number(self, wordification):
        """
            Outputs full-number version of a given wordification
        """
        # for character in string, just translate it. Should be trivial.
        print("")
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

        # TODO redundancy check here? pare down of repeats, like?
        # to eliminate the DOG|333 vs DOG|3|33 vs DOG|3|3|3 issue. Compare the final concatenated string versions, and keep only the best score.

        # TODO I think this is where the recording of whether things are words or not words or where they are will happen
        # TODO and to a larger extend the creation of the wordification objects
        # for score, just to get this down: the more translated letters you have, the better. The less words, the better.
        # the more all-number chunks, the worse. if there's exactly 1, 4, or 7 all number chunks, they don't count against you.
        # the last all-number-chunk at the end doesn't count either(?)
        # differentiate numbers and letters based whether the first one is a letter or a number
        return possible_resultant_strings

    def all_substring_sets(self, test_string):
        """
            Returns a list of all the possible subdivisions that can be made by slicing the provided string any
            number of times without changing its order.
        """
        # TODO make this static and useful for any string or...?
        # TODO substrings is a bad name here
        slice_set_list = []
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
                slice_set_list.append([test_string])

            # iterate through each slice, storing the resulting segments in the master list
            while not slicing_complete:
                # reset which cut to move to the last most one
                index_of_cut_to_move = len(current_cut_indices) - 1
                # put together the start and end cut points with the current cut indices
                substring_values = [0]
                substring_values.extend(current_cut_indices)
                substring_values.append(len(test_string))
                # do the substring-ing
                slices_for_this_cut_set = []
                for index in range(len(substring_values) - 1):
                    slices_for_this_cut_set.append(test_string[substring_values[index]:substring_values[index + 1]])
                # save this subdivision set in the master list
                slice_set_list.append(slices_for_this_cut_set)

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
                # reset all the following cuts to be together in line after the moved cut
                for cut_number in range(len(current_cut_indices)):
                    if cut_number > index_of_cut_to_move:
                        current_cut_indices[cut_number] = current_cut_indices[cut_number - 1] + 1

        return slice_set_list

    def cut_advance_is_valid(self, current_cut_indices, index_of_cut_to_move, cut_string_length):
        """
            a helper function for all_substring_sets. Return boolean representing if advancing the provided
            cut to move would conflict with any existing cuts or with the limits of the string being cut, as
            determined by the provided set of cut indicies and the length of the cut string
        """
        potential_new_value = current_cut_indices[index_of_cut_to_move] + 1
        too_far = (potential_new_value == cut_string_length)
        conflicts_with_next_cut = False
        # checking the lastmost cut will give an index out of bounds, and it can't conflict with a later cut anyway.
        # So don't check it. 
        if index_of_cut_to_move != (len(current_cut_indices) - 1):
            conflicts_with_next_cut = (potential_new_value == current_cut_indices[index_of_cut_to_move + 1])
        return not (too_far or conflicts_with_next_cut)


    def generate_all_wordifications(self):
        """
            Returns a list of all possible wordifications of this effort's number
        """
        wordifications_list = []

        sets_to_check = self.all_substring_sets()
        # for each set in sets_to_check
        for set in sets_to_check:
            valid_translation_parts = []
            # for each component of that set
            for component in set:
                # get a list of its valid *full* translations
                valid_translations = self.generate_valid_translations(component)
                # TODO valid translations should also include the full-number version of that chunk, but no all-full-number version (??)
                    # chunk object? word / number / score data members?
                    # maybe just leave the all-numbers in there, or filter it out at the end with an equality check?
                # store that list somewhere sensible
                valid_translation_parts.append(valid_translations)
            # add to the final list the every possible in-order concatenation of the valid translations parts
            for wordification in self.merge_and_concatenate_string_lists(valid_translation_parts):
                wordifications_list.append(wordification)
            # TODO gotta actually create the wordification objects too *somewhere*

        return wordifications_list

    def generate_valid_translations(self, component_string):
        """
            Input a string of numbers and return every possible valid full english translation of that string,
            plus the all-numbers variant
        """
        valid_translations = []
        valid_translations.append(component_string)
        # for each number in component string
            # translate it into a list of the letters it could be (lookup)
            # merge those lists with the list-merging method to get all the gibberish words it could be
            # if the word is a real word (method) then add it to the valid translations list
        return valid_translations


    def check_if_valid_english_word(self, string_to_check):
        """ TODO """
        # check word against imported dictionary (?) in smart (??) and efficient (???) way
        # if it's valid return true, if not return false
        return




def main():
    """ nice UI and some tests probably """
    # greet
    # brief summary of wordifications
    # ask if they want to translate a wordification to a number or vice versa, or to exit
        # prompt for phone number
        # object to improper formatting, but allow it anyway on insistance
        # ask if they want the best, all of them, or a random one, or exit to one level out, and supply the choice with the associated calls

    test_merge_and_concatenate = True
    test_all_substring_sets = False

    if test_merge_and_concatenate:
        test_effort = Wordification_Effort("401-867-5309")
        #list_of_lists_of_test_strings = [["I ","You ","We "],["like ","hate "],["vanilla.","chocolate.","strawberry."]]
        list_of_lists_of_test_strings = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
        resulting_strings = test_effort.merge_and_concatenate_string_lists(list_of_lists_of_test_strings)

        for index in range(len(resulting_strings)):
            print(str(index + 1) + ": " + resulting_strings[index])

    if test_all_substring_sets:
        test_effort = Wordification_Effort("401-867-5309")
        test_string = "horse"
        resulting_string_sets = test_effort.all_substring_sets(test_string)
        counter = 1
        print_str = ""
        for set in resulting_string_sets:
            print_str += str(counter) + ": "
            counter += 1
            print_str += str(set) + "\n"
        print(print_str)




if __name__ == "__main__":
    main()

# TODO classes may need some reorganization; some of the methods are gonna be static otherwise, so probably don't include them in the class for clarity?
# TODO reorder methods so that ones that reference other ones come later