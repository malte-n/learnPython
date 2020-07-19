from random import randint, choice
from math import factorial

class Die:
    def __init__(self, sides=0):
        self.sides = sides


    def roll_die(self):
        rolled_die = randint(1, self.sides)
        print(rolled_die)



    def lottery_list(self):
        list_of_lottery_options = ['1', '2', '3','4','5','6','7','8','9','10','a','b','c','d','e']
        my_ticket=['4', 'a', '8', '2']
        selected_options = []
        number_of_runs = 0


        def npermutations(l):
            length_of_options = len(l)
            length_of_code = len(my_ticket)
            num = factorial(length_of_options)
            den = factorial(length_of_options-length_of_code)
            return int(num/den)


        def find_matching_lotto():
            x = 0
            selected_options.clear()
            list_of_lottery_options_copy = list_of_lottery_options[:]
            while x < 4:

                index_to_pop = randint(0, (len(list_of_lottery_options_copy)-1))
                selected_option = list_of_lottery_options_copy.pop(index_to_pop)
                selected_options.append(selected_option)
                x = x + 1
            print(f"The ticket with the following Values wins: {selected_options[0]}, {selected_options[1]}, {selected_options[2]}, {selected_options[3]}")
            list_of_lottery_options_copy.clear()

        while my_ticket != selected_options:
            find_matching_lotto()
            number_of_runs += 1

        probability = npermutations(list_of_lottery_options)

        print(f"You have won! It ran {number_of_runs}. The probability was 1/{probability}.")

die_6 = Die(20)

die_6.lottery_list()
