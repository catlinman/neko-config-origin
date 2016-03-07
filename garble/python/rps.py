
import math
import random

# Simple extendable Rock, Paper, Scissors game I wrote to teach a friend
# Python. Code should be rather self explanitory.


class rps_selection:

    def __init__(self, name, abb):
        self.name = name
        self.abbreviation = abb
        self.counters = {}

    def add_counter(self, sel):
        self.counters[sel.abbreviation] = sel

    def is_counter(self, sel):
        if sel.abbreviation in self.counters:
            return True

        else:
            return False

    def is_equal(self, sel):
        if sel.abbreviation == self.abbreviation:
            return True

        else:
            return False


class rps_game:

    def __init__(self, limit):
        self.limit = limit
        self.round = 0
        self.wins = 0
        self.goal = math.ceil(self.limit / 2)
        self.selections = {}
        self.selection_string = ""

    def add_selection(self, sel):
        self.selections[sel.abbreviation] = sel

    def start_game(self):
        # Game logic here.
        print("Starting a new game of Rock, Paper, Scissors!")

        self.selection_string = ""

        for abb in self.selections:
            sel = self.selections[abb]
            self.selection_string += " {}({})".format(sel.name,
                                                      sel.abbreviation)

        print("Possible choices are:{}".format(self.selection_string))

        while self.wins < self.goal and self.round - self.wins < self.goal:
            self.start_round()

        if self.wins >= self.goal:
            print("You have won the game!")

        else:
            print("The computer won the game!")

        print("Rounds played: {}".format(self.round))
        print("Final points: You {} / Com {})".format(
            self.wins, self.round - self.wins))

    def start_round(self):
        if self.round == 0:
            print("Starting round {}!".format(self.round + 1))

        else:
            print("Starting round {}! Points: You {} / Com {}".format(
                self.round + 1, self.wins, self.round - self.wins))

        user_input = ""
        while not user_input:
            user_input = input("Make your choice (abbreviation): ")

            if not user_input in self.selections:
                user_input = ""
                print("Not a choice. Possible choices are:{}".format(
                    self.selection_string))

        user_selection = self.selections[user_input]

        computer_selection = self.selections[
            random.choice(list(self.selections.keys()))]

        print("You played {}. The computer played {}.".format(
            user_selection.name, computer_selection.name))

        if not computer_selection.is_equal(user_selection):
            outcome = computer_selection.is_counter(user_selection)

            if not outcome:
                print("The computer won the round!")

            else:
                print("You won the round!")
                self.wins += 1

            self.round += 1

        else:
            print("You both chose the same option. Draw!")

game = rps_game(5)

rock = rps_selection("Rock", "r")
paper = rps_selection("Paper", "p")
scissors = rps_selection("Scissors", "s")

rock.add_counter(paper)
paper.add_counter(scissors)
scissors.add_counter(rock)

game.add_selection(rock)
game.add_selection(paper)
game.add_selection(scissors)

game.start_game()
