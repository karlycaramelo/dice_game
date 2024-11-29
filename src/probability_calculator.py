# This file contains the ProbabilityCalculator class which is responsible for calculating the probability of winning for a given pair of dice.
class ProbabilityCalculator:
    @staticmethod 
    def calculate_win_probability(dice1, dice2):
        dice1_wins = 0
        total_outcomes = len(dice1) * len(dice2)

        for value1 in dice1:
            for value2 in dice2:
                if value1 > value2:
                    dice1_wins += 1
        
        return dice1_wins / total_outcomes
