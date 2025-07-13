# Importing the tkinter module for GUI creation
import tkinter as tk

# Importing messagebox for pop-up dialogs
from tkinter import messagebox

# Importing math module for infinite values used in Minimax
import math

# Define the TicTacToe class
class TicTacToe:
    # Constructor to initialize the game
    def __init__(self, root):
        self.root = root  # Store the main tkinter window
        self.root.title("Tic-Tac-Toe (You: X | Computer: O)")  # Set the window title

        self.board = [' ' for _ in range(9)]  # Initialize the board with 9 empty spaces
        self.buttons = []  # List to store button widgets

        self.create_board()  # Create the GUI board
        self.player = 'X'  # Set player symbol
        self.computer = 'O'  # Set computer symbol

    # Method to create the game board using buttons
    def create_board(self):
        for i in range(9):  # Loop through 9 grid positions
            # Create a button with a command that calls on_click(i) when clicked
            button = tk.Button(self.root, text=' ', font='Helvetica 20 bold', height=3, width=6,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)  # Position the button in a 3x3 grid
            self.buttons.append(button)  # Add the button to the list

    # Method to handle a button click
    def on_click(self, index):
        if self.board[index] == ' ':  # Check if the clicked cell is empty
            self.make_move(index, self.player)  # Player makes a move

            # Check if the player won
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "You win!")  # Show win message
                self.reset_board()  # Reset the board
                return
            # Check for a draw
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")  # Show draw message
                self.reset_board()  # Reset the board
                return

            self.root.after(500, self.computer_move)  # Wait 0.5s then make computer move

    # Method to make a move for the given player at the given index
    def make_move(self, index, player):
        self.board[index] = player  # Update the board
        self.buttons[index]['text'] = player  # Update the button's text
        self.buttons[index]['state'] = 'disabled'  # Disable the button

    # Method to check if the game is a draw
    def is_draw(self):
        return ' ' not in self.board  # True if no empty spaces left

    # Method to check if a given player has won
    def check_winner(self, player):
        # All possible winning combinations (rows, columns, diagonals)
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]
        # Check if any winning combination is occupied entirely by the player
        return any(all(self.board[i] == player for i in combo) for combo in win_combinations)

    # Method for the computer to make its move
    def computer_move(self):
        best_score = -math.inf  # Initialize best score to negative infinity
        best_move = None  # Initialize best move

        for move in self.available_moves():  # Check all available moves
            self.board[move] = self.computer  # Try the move
            score = self.minimax(0, False)  # Evaluate the move using minimax
            self.board[move] = ' '  # Undo the move

            if score > best_score:  # Check if this move is better
                best_score = score  # Update best score
                best_move = move  # Update best move

        self.make_move(best_move, self.computer)  # Make the best move

        # Check if computer won
        if self.check_winner(self.computer):
            messagebox.showinfo("Game Over", "Computer wins!")  # Show win message
            self.reset_board()  # Reset board
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")  # Show draw message
            self.reset_board()  # Reset board

    # Minimax algorithm for evaluating moves
    def minimax(self, depth, is_maximizing):
        # Base cases for win/loss/draw
        if self.check_winner(self.computer):
            return 1  # Computer wins
        elif self.check_winner(self.player):
            return -1  # Player wins
        elif self.is_draw():
            return 0  # Draw

        if is_maximizing:
            best_score = -math.inf  # Initialize max score
            for move in self.available_moves():
                self.board[move] = self.computer  # Try move
                score = self.minimax(depth + 1, False)  # Recurse
                self.board[move] = ' '  # Undo move
                best_score = max(score, best_score)  # Choose highest score
            return best_score
        else:
            best_score = math.inf  # Initialize min score
            for move in self.available_moves():
                self.board[move] = self.player  # Try move
                score = self.minimax(depth + 1, True)  # Recurse
                self.board[move] = ' '  # Undo move
                best_score = min(score, best_score)  # Choose lowest score
            return best_score

    # Return a list of available (empty) positions on the board
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # Reset the game board for a new round
    def reset_board(self):
        self.board = [' ' for _ in range(9)]  # Clear the board
        for btn in self.buttons:
            btn.config(text=' ', state='normal')  # Reset button text and enable

# Main function to start the game
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = TicTacToe(root)  # Create the game instance
    root.mainloop()  # Start the GUI event loop
