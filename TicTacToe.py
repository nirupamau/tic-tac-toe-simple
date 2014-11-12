import TicTacBoard
import TicTacEngine
import Player
import turtle

class TicTacToe:
        def __init__(self):
                self.board = TicTacBoard.TicTacBoard()
                self.engine = TicTacEngine.TicTacEngine()
                self.player1 = Player.Player("Player 1", 'X', "blue")
                self.player2 = Player.Player("Player 2", 'O', "red")
                self.isOver = False
                self.startGame()
                self.positionPl1 = 0
                self.positionPl2 = 0

        def startGame(self):
                while True:
                        print( "Cleaning board, and starting new Game")
                        self.isOver = False
                        self.board.cleanBoard()
                        self.board.drawBoard()
                        self.engine.initialize()
                        while not self.isOver:
                                self.positionPl1 = self.PlayerInput()
                                while((self.validityCheck(self.positionPl1)) is False):
                                        self.positionPl1 = self.PlayerInput()
                                self.isOver = self.board.updateBoard(self.positionPl1, self.player1)
                                if(self.isOver):
                                        break
                                self.positionPl2 = self.PlayerInput()
                                while ((self.validityCheck(self.positionPl2))is False):
                                        self.positionPl2 = self.PlayerInput()
                                self.isOver = self.board.updateBoard(self.positionPl2, self.player2)
                                if(self.isOver):
                                        break
                                self.engine.printIt()
                                
        def PlayerInput(self):
                return int(input("Enter an empty box number on the board:"))

        def validityCheck(self, pos):
                if pos in range(0,9):
                        if(self.engine.state[pos]==0):
                                self.engine.state[pos] = 1
                                return True
                        else:
                                print ("Invalid Input, try again1")
                                return False
                else:
                        return False
                                
               
game = TicTacToe()
game.startGame()
