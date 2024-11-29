from random_generator import RandomGenerator
from probability_table_generator import ProbabilityTableGenerator
import sys

# Class that represents a dice game.
class DiceGame:
    def __init__(self, dice_list):
        self.dice_list = dice_list
        self.random_gen = RandomGenerator()

    def determine_first_move(self):
        print("Let's determine who makes the first move.")
        random_number = self.random_gen.generate_number(2)
        hmac_value, key = self.random_gen.generate_hmac(random_number)
        print(f"I selected a random value in the range 0..1 (HMAC={hmac_value}).")
        print("Try to guess my selection.")
        print("0 - 0")
        print("1 - 1")
        print("X - exit")
        print("? - help")
        user_input = input("Your selection: ").strip().upper()

        if user_input == "X":
            exit(0)
        elif user_input == "?":
            ProbabilityTableGenerator.generate_table(self.dice_list)
            exit(0)
        elif user_input not in ["0", "1"]:
            print("Invalid selection. Exiting.")
            exit(1)

        print(f"My selection: {random_number} (KEY={key}).")
        return int(user_input) == random_number

    def play_round(self, user_first):
        if user_first:
            print("Choose your dice:")
            for i, dice in enumerate(self.dice_list):
                print(f"{i} - {dice}")
            print("X - exit")
            print("? - help")
            user_choice = input("Your selection: ").strip().upper()

            if user_choice == "X":
                sys.exit(0)
            elif user_choice == "?":
                ProbabilityTableGenerator.generate_table(self.dice_list)
                sys.exit(0)

            user_dice = self.dice_list[int(user_choice)]
            print(f"You choose the {user_dice} dice.")
            self.dice_list.pop(int(user_choice))

            computer_dice = self.dice_list[self.random_gen.generate_number(len(self.dice_list))]
            print(f"I choose the {computer_dice} dice.")
        else:
            computer_dice = self.dice_list[self.random_gen.generate_number(len(self.dice_list))]
            print(f"I make the first move and choose the {computer_dice} dice.")
            self.dice_list.remove(computer_dice)

            print("Choose your dice:")
            for i, dice in enumerate(self.dice_list):
                print(f"{i} - {dice}")
            print("X - exit")
            print("? - help")
            user_choice = input("Your selection: ").strip().upper()

            if user_choice == "X":
                sys.exit(0)
            elif user_choice == "?":
                ProbabilityTableGenerator.generate_table(self.dice_list)
                sys.exit(0)

            user_dice = self.dice_list[int(user_choice)]
            print(f"You choose the {user_dice} dice.")

        return user_dice, computer_dice

    def perform_throws(self, user_dice, computer_dice):
        print("It's time for my throw.")
        computer_random = self.random_gen.generate_number(6)
        hmac_value, key = self.random_gen.generate_hmac(computer_random)
        print(f"I selected a random value in the range 0..5 (HMAC={hmac_value}).")
        print("Add your number modulo 6.")
        for i in range(6):
            print(f"{i} - {i}")
        print("X - exit")
        user_input = input("Your selection: ").strip().upper()

        if user_input == "X":
            sys.exit(0)

        computer_result_index = (computer_random + int(user_input)) % 6
        computer_throw = computer_dice[computer_result_index]
        print(f"My number is {computer_random} (KEY={key}).")
        print(f"The result is {computer_random} + {user_input} = {computer_result_index} (mod 6).")
        print(f"My throw is {computer_throw}.")

        print("It's time for your throw.")
        user_random = self.random_gen.generate_number(6)
        hmac_value, key = self.random_gen.generate_hmac(user_random)
        print(f"I selected a random value in the range 0..5 (HMAC={hmac_value}).")
        print("Add your number modulo 6.")
        for i in range(6):
            print(f"{i} - {i}")
        print("X - exit")
        user_input = input("Your selection: ").strip().upper()

        if user_input == "X":
            sys.exit(0)

        user_result_index = (user_random + int(user_input)) % 6
        user_throw = user_dice[user_result_index]
        print(f"My number is {user_random} (KEY={key}).")
        print(f"The result is {user_random} + {user_input} = {user_result_index} (mod 6).")
        print(f"Your throw is {user_throw}.")

        return user_throw, computer_throw
