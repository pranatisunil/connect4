"""
Board module for Connect Four game.
Handles the game board state and operations.
"""

class Board:
    """A data type for a Connect Four board with arbitrary dimensions."""
    
    def __init__(self, height, width):
        """
        Constructs a new Board object.
        
        Args:
            height: Number of rows (typically 6)
            width: Number of columns (typically 7)
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for _ in range(self.height)]

    def __repr__(self):
        """Returns a string representation of the Board."""
        s = ''
        
        # Add the rows with checkers
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        
        # Add the bottom border
        s += '-' * (self.width * 2 + 1) + '\n'
        
        # Add the column numbers
        s += ' '
        for col in range(self.width):
            s += str(col % 10) + ' '
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """
        Adds a checker to the specified column.
        
        Args:
            checker: Either 'X' or 'O'
            col: Column index (0 to width-1)
            
        Raises:
            AssertionError: If invalid checker or column
        """
        assert checker in ('X', 'O'), "Checker must be 'X' or 'O'"
        assert 0 <= col < self.width, "Column out of bounds"
        
        for row in range(self.height - 1, -1, -1):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                return

    def reset(self):
        """Resets the Board to be empty."""
        self.slots = [[' '] * self.width for _ in range(self.height)]

    def can_add_to(self, col):
        """
        Checks if a checker can be added to the column.
        
        Args:
            col: Column index to check
            
        Returns:
            bool: True if column has space, False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.slots[0][col] == ' '

    def is_full(self):
        """Checks if the board is completely full."""
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self, col):
        """
        Removes the top checker from the column.
        
        Args:
            col: Column index to remove from
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return

    def is_win_for(self, checker):
        """
        Checks if the specified checker has won.
        
        Args:
            checker: Either 'X' or 'O'
            
        Returns:
            bool: True if checker has won, False otherwise
        """
        assert checker in ('X', 'O'), "Invalid checker"
        
        # Check all possible win conditions
        return (self._is_horizontal_win(checker) or
                self._is_vertical_win(checker) or
                self._is_down_diagonal_win(checker) or
                self._is_up_diagonal_win(checker))

    def _is_horizontal_win(self, checker):
        """Checks for horizontal win."""
        for row in range(self.height):
            for col in range(self.width - 3):
                if all(self.slots[row][col + i] == checker for i in range(4)):
                    return True
        return False

    def _is_vertical_win(self, checker):
        """Checks for vertical win."""
        for col in range(self.width):
            for row in range(self.height - 3):
                if all(self.slots[row + i][col] == checker for i in range(4)):
                    return True
        return False

    def _is_down_diagonal_win(self, checker):
        """Checks for down diagonal win (top-left to bottom-right)."""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if all(self.slots[row + i][col + i] == checker for i in range(4)):
                    return True
        return False

    def _is_up_diagonal_win(self, checker):
        """Checks for up diagonal win (bottom-left to top-right)."""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if all(self.slots[row - i][col + i] == checker for i in range(4)):
                    return True
        return False
