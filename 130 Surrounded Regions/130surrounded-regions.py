class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0
        # iterate over edges of the board, lock in all guys connected to them
        # everything else change to X
        def save(r, c):
            if r < 0 or r > len(board)-1 or c < 0 or c > len(board[0])-1 or board[r][c] != 'O':
                return
            board[r][c] = 'S'
            for dr, dc in dirs:
                save(r + dr, c + dc)
        
        for c in range(len(board[0])):
            save(0, c)
            save(len(board)-1, c)
        
        for r in range(len(board)):
            save(r, 0)
            save(r, len(board[0])-1)


        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = 'O' if board[r][c] == 'S' else 'X'

        
                
