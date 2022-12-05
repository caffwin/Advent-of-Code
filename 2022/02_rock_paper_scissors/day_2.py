TEST_INPUT_FILE = "test_input.txt"

# Outcome of round
# draw = 3, win = 6, lose = 0
ROCK_PAPER_SCISSORS_OUTCOME_DICT = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B Y": 3,
    "B X": 0,
    "B Z": 6,
    "C Z": 3,
    "C X": 6,
    "C Y": 0
}

ROCK_PAPER_SCISSORS_OUTCOME_DICT_P2 = {
    "A X": [0, "scissors"], # l
    "A Y": [3, "rock"], # d
    "A Z": [6, "paper"], # d
    "B X": [0, "rock"], # w
    "B Y": [3, "paper"], # d 
    "B Z": [6, "scissors"], # w
    "C X": [0, "paper"], # l
    "C Y": [3, "scissors"], # d
    "C Z": [6, "rock"] # w    
}


ROCK_PAPER_SCISSORS_SCORE_DICT_P2 = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

ROCK_PAPER_SCISSORS_SCORE_DICT = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def calc_match_total_p2(strategy_guide_pair):
    your_shape = ROCK_PAPER_SCISSORS_OUTCOME_DICT_P2[strategy_guide_pair][1]
    outcome_score = ROCK_PAPER_SCISSORS_OUTCOME_DICT_P2[strategy_guide_pair][0]
    shape_score = ROCK_PAPER_SCISSORS_SCORE_DICT_P2[your_shape]
    return int(outcome_score + shape_score)

def calc_strategy_guide_total_score(TEST_INPUT_FILE):
    sum_score = 0
    p2_score = 0
    with open(TEST_INPUT_FILE) as file:
        for line in file:
            stripped_line = line.strip()
            match_score = calculate_match_total(stripped_line)
            sum_score += match_score
            p2_score += calc_match_total_p2(stripped_line)

    return sum_score, p2_score

def calculate_match_total(strategy_guide_pair):
    """
    Total is calculated the sum of two scores: outcome of round, value of shape.

    Takes in a single pair of shapes played by opponent and you as input 
    First column: opponent's shape
    Second column: your shape
    """

    your_shape = strategy_guide_pair[-1]
    outcome_score = ROCK_PAPER_SCISSORS_OUTCOME_DICT[strategy_guide_pair]
    shape_score = ROCK_PAPER_SCISSORS_SCORE_DICT[your_shape]
    return int(outcome_score + shape_score)

def run():
    p1_solution, p2_solution = calc_strategy_guide_total_score(TEST_INPUT_FILE)
    print("part one solution: ", p1_solution)
    print("part two solution:", p2_solution)
    return

if __name__ == "__main__":
    run()