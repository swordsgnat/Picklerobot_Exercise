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
        possible_resultant_strings = []

        # make a list of indicies for each list in the list of lists
        # start em' all at zero
        # increment the first one
        # if it hits its end, zero it and increment the next one (if that one hits it's end, ditto, etc.)
        # concatenate all those indices of those lists together

        # TODO redundancy check here? pare down of repeats, like?
        # to eliminate the DOG|333 vs DOG|3|33 vs DOG|3|3|3 issue, yeah. Just compare the final concatenated string versions, and keep only the best score.

        # TODO I think this is where the recording of whether things are words or not words or where they are will happen
        # TODO and to a larger extend the creation of the wordification objects
        # for score, just to get this down: the more translated letters you have, the better. The less words, the better.
        # the more all-number chunks, the worse. if there's exactly 1, 4, or 7 all number chunks, they don't count against you.
        # the last all-number-chunk at the end doesn't count either(?)
        # differentiate numbers and letters based whether the first one is a letter or a number
        return possible_resultant_strings

    def all_substring_sets(self):
        """
            Returns a list of all the possible substrings sets that can be made by slicing the phone number
            number of times without changing its order.
        """
        substring_set_list = []
        # do the operation on self.phone_number
        # (or on a given string, for versatility? maybe the class is more trouble than it's worth?)
        # cut paradigm
        # for all possible numbers of cuts (zero to one minus the number of characters in the string we're sub stringing)
            # create a list of cut indicies with that # of entries
            # the first element of the list starts at zero, each subsequent is plus one each starting at one more than the last (first at 0)
            # record a second list of "starting points" (?)
            # move through all the valid cut configurations
                # that is, increment the last cut. The end and beginning don't count, so min is one and max is size - one, ish
                # If you can't validly increment the last cut, add one to the start index of the next one up the chain and reset the current indicies to the start ones
                # subsection the string according to those indicies
                    # that is, first do the subsection of the first cut, then of the first to the second, then of the second to the third, then of just the third to the end, for example
                # add the subsections to the list
        return substring_set_list

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


if __name__ == "__main__":
    main()

# TODO classes may need some reorganization; some of the methods are gonna be static otherwise, so probably don't include them in the class for clarity?
# TODO reorder methods so that ones that reference other ones come later