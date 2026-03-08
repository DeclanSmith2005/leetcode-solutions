class TicTacToe:

    def __init__(self, n: int):
        self.board = [['.' for i in range(n)] for k in range(n)]
        self.indicies= [0 for i in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        #row
        for r in self.board:
            if all(i == player for i in r):
                return player
        # col
        for c in range(len(self.board[0])):
            curr = True
            for r in range(len(self.board[0])-1):
                if self.board[r][c] != self.board[r+1][c] or self.board[r][c] == '.' or self.board[r+1][c] == '.':
                    curr = False
            if curr == True:
                return player  
        # top left bottom right diagonal
        r, c = (0, 0)
        curr = True
        while r < len(self.board)-1:
            if self.board[r][c] != self.board[r+1][c+1]  or self.board[r][c] == '.' or self.board[r+1][c+1] == '.':
                    curr = False
            r, c  = r + 1, c+ 1
        if curr == True:
                return player
        #bottom left, top right diagonal 
        r, c = (len(self.board)-1, 0)
        curr = True
        while c < len(self.board)-1:
            if self.board[r][c] != self.board[r-1][c+1] or self.board[r][c] == '.' or self.board[r-1][c+1] == '.' :
                    curr = False
            r, c  = r - 1, c+ 1
        if curr == True:
                return player 
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)