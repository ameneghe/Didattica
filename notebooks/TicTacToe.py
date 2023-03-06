class Tris:
    
    def __init__(self):
        self.states = { 'S':-1, 'D':0, 'V':1, 'C':-2}
        self.opposite = { 'x':'o', 'o':'x', ' ':' ', 'V':'S', 'S':'V', 'D':'D', 'C':'C' }
        self.reset()
        
        
    def reset(self):
        self.table = [' ' for i in range(9) ]
        self.counter = 0
        
    
    def print(self):
        for k in range(3):
            print(  "", self.table[0+k*3], "|", self.table[1+k*3], "|", self.table[2+k*3] )
            if k<2: print("---+---+---")
            

    def checkTris(self,symbol):
        dirs = [ (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6) ]
        for d in dirs:
            if all( self.table[i] == symbol for i in d ):
                return True
        return False
        

    def put(self,i,symbol):
        if i>=0 and i<9 and self.table[i] == ' ':
            self.table[i] = symbol
            self.counter+=1
            return True
        return False
    
    
    def movePlayer(self,symbol):
        i = 0
        while not self.put( i-1, symbol ):
             try: i = int(input("Insert cell (1-9): ")) 
             except ValueError: i = 0
     

    def moveComputer(self, symbol):
        (scoreMax,iMax) = ('C', -1)
        for i in range(9):
            if self.put( i, symbol ):
                if self.checkTris(symbol):
                    (scoreMax,iMax) = ('V',i)
                elif self.counter>=9 and scoreMax!='V':
                    (scoreMax,iMax) = ('D',i)
                else:
                    (score,j) = self.moveComputer(self.opposite[symbol])
                    score = self.opposite[score]
                    if self.states[score] > self.states[scoreMax]:
                        (scoreMax, iMax) = (score,i)
                self.table[i] = ' '
                self.counter -= 1
        return (scoreMax,iMax)
        
    
    def menu(self):
        (symbol,turn) = (' ',-1)
        while symbol !='o' and symbol !='x':
            symbol = input("Select your symbol (x|o): ")
        while turn!='y' and turn!='n':
            turn = input("Do you want to start first? (y|n): ")
        return (symbol,int(turn!='y'))
    
    
    def play(self, symbol, turn):
        state = 'C'
        symbol2 = self.opposite[symbol]
        while self.counter<9 and state == 'C':
            
            if self.counter%2 == turn:
                self.movePlayer( symbol )
                if self.checkTris( symbol ): state = 'V'
            else: 
                (score,i) = self.moveComputer( symbol2 )
                self.put( i, symbol2 )
                print("\nComputer's turn: ",i+1)
                if self.checkTris( symbol2 ): state = 'S'
                
            self.print()            
            
        message = { 'V' : "You Win!", 'S' : "You Lose!" }
        print( message.get(state, "Draw") )


    def main(self):
        while True:
            self.reset()
            (symbol,turn) = self.menu()
            self.play(symbol,turn)
            if input("Do you wanto to play again? (y|n) ") != 'y':
                break


tris = Tris()
tris.main()

