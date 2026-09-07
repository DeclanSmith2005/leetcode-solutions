class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])
        changed = False
        while True:
            changed = False
            final = set()
            for i in range(n): #horizontal traversal
                coords = set()
                value = None
                for j in range(m):
                    if board[i][j] == value and value != 0:
                        coords.add((i, j))
                    else:
                        if len(coords) >= 3:
                            changed = True
                            final |= coords
                        coords = {(i, j)}
                        value = board[i][j]
                if len(coords) >= 3:
                    changed = True
                    final |= coords
            for j in range(m):
                coords = set()
                value = None
                for i in range(n):
                    if board[i][j] == value and value != 0:
                        coords.add((i, j))
                    else:
                        if len(coords) >= 3:
                            changed = True
                            final |= coords
                        coords = {(i, j)}
                        value = board[i][j]
                if len(coords) >= 3:
                    changed = True
                    final |= coords
            if not changed:
                return board
            for x, y in final:
                board[x][y] = 0
            
            # drop blocks down
            for j in range(m):
                wi = n-1
                for ri in range(n-1, -1, -1):
                    if board[ri][j] == 0:
                        continue
                    board[wi][j], board[ri][j] = board[ri][j], board[wi][j]
                    wi -= 1
                    


        return board