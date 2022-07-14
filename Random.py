import Board
import random

def ran_simulate(board, turn, team_loc):
    dice = random.randint(1, 6)
    next_move = random.choice(get_possibleChess(board, turn, team_loc, dice))
    return next_move
