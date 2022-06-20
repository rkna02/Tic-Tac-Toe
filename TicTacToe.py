# student name: Peter Na
# student number: 36734671
import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played)
            and prints the banner messages
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell,
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()


    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        print("\r")
        print(f"   {self.board[0]} | {self.board[1]} | {self.board[2]}    0 | 1 | 2")
        print("   --+---+--    --+---+--")
        print(f"   {self.board[3]} | {self.board[4]} | {self.board[5]}    3 | 4 | 5")
        print("   --+---+--    --+---+--")
        print(f"   {self.board[6]} | {self.board[7]} | {self.board[8]}    6 | 7 | 8")
        print("\r")


    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number;
            error checks that the input is a valid cell number;
            and prints the info and the updated self.board;
        """
        while True:
            # continuously prompt for user input until it is valid
            nextMove = input("Next move for X (state a valid cell num): ")

            if not nextMove.isdigit():
                print("Must be an integer")
            elif type(eval(nextMove)) == float:
                print("Must be an integer")
            elif eval(nextMove) < 0 or eval(nextMove) > 8 or eval(nextMove) in self.played:
                print("Must enter a valid cell number")
            else:
                self.board[eval(nextMove)] = "X"
                self.played.add(eval(nextMove))
                print(f"You chose cell {eval(nextMove)}")
                self.printBoard()
                break


    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell,
            and prints the info and the updated self.board
        """
        # loop until a valid integer is generated
        nextMove = random.randint(0, 8)
        while nextMove in self.played:
            nextMove = random.randint(0, 8)

        # updates info and board
        self.board[nextMove] = "O"
        self.played.add(nextMove)
        print(f"Computer chose cell {nextMove}")
        self.printBoard()


    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        hasWon = False
        if self.board[0] == who and self.board[1] == who and self.board[2] == who:
            hasWon = True
        elif self.board[3] == who and self.board[4] == who and self.board[5] == who:
            hasWon = True
        elif self.board[6] == who and self.board[7] == who and self.board[8] == who:
            hasWon = True
        elif self.board[0] == who and self.board[3] == who and self.board[6] == who:
            hasWon = True
        elif self.board[1] == who and self.board[4] == who and self.board[7] == who:
            hasWon = True
        elif self.board[2] == who and self.board[5] == who and self.board[8] == who:
            hasWon = True
        elif self.board[0] == who and self.board[4] == who and self.board[8] == who:
            hasWon = True
        elif self.board[2] == who and self.board[4] == who and self.board[6] == who:
            hasWon = True

        return hasWon


    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or
                 "You lost! Thanks for playing." or
                 "A draw! Thanks for playing."
        """
        terminate = False
        if len(self.played) == 9 and not self.hasWon("X") and not self.hasWon("O"):
            print("A draw! Thanks for playing.")
            terminate = True
        elif self.hasWon("X"):
            print("You won! Thanks for playing.")
            terminate = True
        elif self.hasWon("O"):
            print("You lost! Thanks for playing.")
            terminate = True

        return terminate

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate