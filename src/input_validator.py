# This file contains the InputValidator class which is responsible for validating the input arguments.
class InputValidator:
    @staticmethod # This method validates the input arguments and returns a list of dice configurations.
    def validate_input(args):
        if len(args) < 3:
            print("Error: You must specify at least 3 dice configurations.")
            print("Example: python main.py 2,2,4,4,9,9 1,1,6,6,8,8 3,3,5,5,7,7")
            exit(1)

        dice_list = []
        for arg in args:
            parts = arg.split(",")
            if len(parts) != 6 or not all(part.isdigit() for part in parts):
                print(f"Error: Invalid dice configuration '{arg}'. Must be 6 integers separated by commas.")
                exit(1)
            dice_list.append(list(map(int, parts)))

        return dice_list
