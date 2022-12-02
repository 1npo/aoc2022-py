# Points added to score based on your choice (RPS)
shape_scores = {0: 1, 1: 2, 2: 3}

# Map AX/BY/CZ to 0/1/2, so we can use bitwise operations to solve the puzzle
shapes = {
    'A': 0, # Rock = 0
    'X': 0, # Rock = 0
    'B': 1, # Paper = 1
    'Y': 1, # Paper = 1
    'C': 2, # Scissors = 2
    'Z': 2, # Scissors = 2
}

# Map X/Y/Z to 0/1/2, so they can be used as a tuple index
part2_needs = {
    'X': 0, # X = Need to lose
    'Y': 1, # Y = Need to draw
    'Z': 2, # Z = Need to win
}

# Define a map to find the required outcome for part 2. The key is the opponents choice. The value is
# a tuple where index:
#   [0] = what choice loses against the opponent (represented as 0/1/2)
#   [1] = what choice draws against the opponent (represented as 0/1/2)
#   [2] = what choice wins against the opponent (represented as 0/1/2)
#
# Take "A X" for example. The opponent picked "rock" (A), and we need to lose (X). "Scissors" loses
# to "rock". So if we look in index [0] of the tuple, we find 2, which represents scissors.
part2_outcomes = {
#         W  D  L
    'A': (2, 0, 1), # R wins against S, draws against R, loses to P
    'B': (0, 1, 2), # P wins against R, draws against P, loses to S
    'C': (1, 2, 0), # S wins against P, draws against S, loses to R
}


# Determine the winner using bitwise operations.
#
# Player 1 (opponent)   = 1
# Player 2 (you)        = 0
# Rock                  = 00 (integer 0)
# Paper                 = 01 (integer 1)
# Scissors              = 10 (integer 2)
#
# 1. If Player 1 and Player 2 make the same choice, the game is a draw.
#   - Return without bit operations.
#   - Otherwise continue.
# 2. Get binary representation of Player 1 by returning 1 shifted 2 bits to the left (100)
# 3. Get binary representation of Player 2 by returning 0 shifted 2 bits to the left (000)
# 4. Use an OR operation to combine the player's representation and their choice of RPS
# 5. Subtract the Player 2 combination from the Player 1 combination
# 6. If the difference is a multiple of 3, you win.
# 7. Otheriwse, your opponent wins.
def get_round_score(opponent: str, you: str):
    if opponent == you:
        return 3 + shape_scores[you]
    
    if (((opponent | 1 << 2) - (you | 0 << 2)) % 3):
        return 0 + shape_scores[you]
    
    return 6 + shape_scores[you]


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [line.strip().split() for line in f]
        
        total_score_part1 = 0
        total_score_part2 = 0

        for rps in content:
            required_outcome = part2_needs[rps[1]]
            you_part2 = part2_outcomes[rps[0]][required_outcome]
            
            total_score_part1 += get_round_score(shapes[rps[0]], shapes[rps[1]])
            total_score_part2 += get_round_score(shapes[rps[0]], you_part2)

    print(f'[+] Part 1 solution: {total_score_part1}')
    print(f'[+] Part 2 solution: {total_score_part2}')

