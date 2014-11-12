import TicTacBoard
class TicTacEngine:
        state = [0,0,0,0,0,0,0,0,0]
        symbols = [['0','1','2'],['3','4','5'],['6','7','8']]
        def isGameNotOver(self): 
                return(self.isRowWinning() or self.isColWinning() or self.isDiagWinning())

        def initialize(self):
                for i in range(0,9):
                        self.state[i] = 0
                for i in range(0,3):
                        for j in range(0,3):
                                self.symbols[i][j]=i*3+j
                
        def isRowWinning(self):
                boolValue = False
                for i in range(0,3):
                        boolValue = boolValue or self.all_same((self.symbols)[i])
                return boolValue

        def all_same(self,items):
                return all(x == items[0] for x in items)
                        
                        

        def isColWinning(self):
                boolValue = True
                for i in range(0,3):
                        sym = self.symbols[0][i]
                        for j in range(1,3):
                                if sym != self.symbols[j][i]:
                                        boolValue = False
                                        break
                        if boolValue == True and j==2:
                                return True
                        boolValue = True
                return False
                   
        def isDiagWinning(self):
                boolValue1 = True
                boolValue2 = True
                prev1 = self.symbols[0][0]
                prev2 = self.symbols[0][2]
                for i in range(0,3):
                        if prev1!=self.symbols[i][i]:
                                boolValue1 = False
                for i in range(0,3):
                        if prev2!=self.symbols[0+i][2-i]:
                                boolValue2 = False
                return boolValue1 or boolValue2
                        
        def printIt(self):
                for i in range(0,3):
                        print (self.symbols[i])
	
