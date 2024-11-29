from probability_calculator import ProbabilityCalculator
# This class is responsible for generating the probability table.
class ProbabilityTableGenerator:
    @staticmethod
    def generate_table(dice_list):
        headers = [f"User dice v"] + [", ".join(map(str, dice)) for dice in dice_list]
        row_separator = "+" + "+".join(["-" * 13 for _ in range(len(dice_list) + 1)]) + "+"
        print("Probability of the win for the user:")
        print(row_separator)
        print("| " + " | ".join([f"{header:<12}" for header in headers]) + " |")
        print(row_separator)

        for i, dice1 in enumerate(dice_list):
            row = [", ".join(map(str, dice1))]
            for j, dice2 in enumerate(dice_list):
                if i == j:
                    row.append(f"- (0.3333)")
                else:
                    probability = ProbabilityCalculator.calculate_win_probability(dice1, dice2)
                    row.append(f"{probability:.4f}")
            print("| " + " | ".join([f"{cell:<12}" for cell in row]) + " |")
            print(row_separator)
