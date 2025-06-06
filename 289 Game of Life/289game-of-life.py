class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def setCell(board, row, col):
            oringalVal = board[row][col]
            numDead= 0
            numAlive = 0
            rows = len(board)
            cols = len(board[0])

            neighbor_offsets = [
                (-1, -1), (-1, 0), (-1, 1),  
                (0, -1),           (0, 1),   
                (1, -1), (1, 0), (1, 1)    
            ]               

            # 0 -> 1 : 2
            # 1 -> 0 : -1

            for dr, dc in neighbor_offsets:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 1 or board[nr][nc] == -1:
                        numAlive+=1
            if numAlive == 3 and oringalVal == 0:
                board[row][col] = 2
            if numAlive > 3 and oringalVal == 1:
                board[row][col] = -1
            if numAlive < 2 and oringalVal == 1:
                board[row][col] = -1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                setCell(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j]= 1
                if board[i][j] == -1:
                    board[i][j]= 0

        




