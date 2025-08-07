"""
Main module for running a Connect Four game.
Handles the game flow between two players.
"""

from board import Board
from player import Player

def connect_four(p1, p2):
    """ 
    Plays a game of Connect Four between two players.
    
    Args:
        p1: Player object using 'X' or 'O'
        p2: Player object using the opposite checker
        
    Returns:
        Board: The final state of the board
    """
    # Validate players
    if p1.checker not in 'XO' or p2.checker not in 'XO' or p1.checker == p2.checker:
        print('Need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(p1, board):
            return board

        if process_move(p2, board):
            return board

def process_move(player, board):
    """
    Processes a single move for the given player.
    
    Args:
        player: The Player making the move
        board: The current Board state
        
    Returns:
        bool: True if the game is over, False otherwise
    """
    print(f"Player {player}'s turn")
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print(board)
    
    if board.is_win_for(player.checker):
        print(f"{player} wins in {player.num_moves} moves!")
        print("Congratulations!")
        return True
        
    if board.is_full():
        print("It's a tie!")
        return True
        
    return False


if __name__ == "__main__":
    # Example of how to run the game with two human players
    p1 = Player('X')
    p2 = Player('O')
    connect_four(p1, p2)
