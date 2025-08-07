"""
Player module for Connect Four game.
Defines the Player class and its subclasses.
"""

class Player:
    """Represents a player in the Connect Four game."""
    
    def __init__(self, checker):
        """
        Initializes a new Player.
        
        Args:
            checker: Either 'X' or 'O'
            
        Raises:
            AssertionError: If checker is not 'X' or 'O'
        """
        assert checker in ('X', 'O'), "Checker must be 'X' or 'O'"
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """Returns a string representation of the Player."""
        return f"Player {self.checker}"
    
    def opponent_checker(self):
        """Returns the opponent's checker."""
        return 'O' if self.checker == 'X' else 'X'
    
    def next_move(self, board):
        """
        Gets the player's next move.
        
        Args:
            board: The current Board state
            
        Returns:
            int: The column number for the next move
        """
        self.num_moves += 1
        while True:
            try:
                col = int(input(f"Enter a column (0-{board.width-1}) for {self.checker}: "))
                if 0 <= col < board.width and board.can_add_to(col):
                    return col
                print("Invalid column. Try again!")
            except ValueError:
                print("Please enter a valid number.")
