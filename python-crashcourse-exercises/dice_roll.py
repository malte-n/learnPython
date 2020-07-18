from random import randint, choice

class Die:
    def __init__(self, sides=0):
        self.sides = sides


    def roll_die(self):
        rolled_die = randint(1, self.sides)
        print(rolled_die)

    def lottery_list(self):
        list_of_lottery_options = ['1', '2', '3','4','5','6','7','8','9','10','a','b','c','d','e']
        list_of_lottery_options_copy = list_of_lottery_options[:]

        selected_options = []
        
        x = 0
        while x < 4:
            index_to_pop = randint(0, (len(list_of_lottery_options_copy)-1))
            selected_option = list_of_lottery_options_copy.pop(index_to_pop)
            selected_options.append(selected_option)
            x = x + 1
        print(f"The ticket with the following Values wins: {selected_options[0]}, {selected_options[1]}, {selected_options[2]}, {selected_options[3]}")
        selected_options.clear()
        list_of_lottery_options_copy.clear()

die_6 = Die(20)

die_6.lottery_list()
