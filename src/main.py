from input_validator import InputValidator
from dice_game import DiceGame

# This is the main entry point of the program.
if __name__ == "__main__":
    import sys
    dice_list = InputValidator.validate_input(sys.argv[1:])
    game = DiceGame(dice_list)
    user_first = game.determine_first_move()
    user_dice, computer_dice = game.play_round(user_first)
    user_throw, computer_throw = game.perform_throws(user_dice, computer_dice)

    if user_throw > computer_throw:
        print(f"You win ({user_throw} > {computer_throw})!")
    elif user_throw < computer_throw:
        print(f"I win ({computer_throw} > {user_throw})!")
    else:
        print(f"It's a draw ({user_throw} = {computer_throw})!")
