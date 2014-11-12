import turtle
import TicTacEngine
class TicTacBoard():
        
        def __init__(self):
                self.brad = turtle.Turtle()
                self.screen = turtle.Screen()
                self.engine = TicTacEngine.TicTacEngine()
                self.myPoints = [[-100,-50],[150,-50],[-100,0],[150,0],[0,100],[0,-150],[50,100],[50,-150]]
                self.points = [[-50,50],[25,50],[100,50],[-50,-25],[25,-25],[100,-25],[-50,-100],[25,-100],[100,-100]]
                self.row = 0
                self.col = 0
        def cleanBoard(self):
                self.brad.clear()
                self.brad.reset()
                
                
        def drawBoard(self):
                i = 0
                j = 0
                while i in range(len(self.myPoints)):
                        self.brad.penup()
                        self.brad.goto(self.myPoints[i][0],self.myPoints[i][1])
                        self.brad.pendown()
                        self.brad.goto(self.myPoints[i+1][0],self.myPoints[i+1][1])
                        i=i+2
                while j in range(len(self.points)):
                        self.brad.penup()
                        self.brad.goto(self.points[j][0],self.points[j][1])
                        self.brad.pendown()
                        self.brad.write(j)
                        j=j+1
		
        def updateBoard(self, position, player):
                self.brad.penup()
                self.brad.goto(self.points[position][0],self.points[position][1])
                self.brad.pendown()
                self.brad.write(" ")
                self.brad.write(player.symbol, font=('Arial',15,'normal'))
                self.row,self.col = self.getRowCol(position)
                print("%d,%d" %(self.row, self.col))
                self.engine.symbols[self.row][self.col] = player.symbol
                boolValue = self.engine.isGameNotOver()
                if(boolValue is True):
                        print( player.name +" is the winner")
                elif((boolValue is False) and 0 not in self.engine.state):
                        print("No winner this time, its a TIE")
                        boolValue = True
                return boolValue

        def getRowCol(self, position):
                count = 0
                if(position<3):
                        return 0,position
                else:
                        while(position>=3):
                                position = position - 3
                                count = count+1
                        return count,position
                                
                
		
