class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row, col, ind, seen):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[ind] or (row, col) in seen:
                return False
            if ind == len(word) -1 and word[-1] == board[row][col]:
                return True
            seen.add((row, col))
            if any(dfs(row + dr, col + dc, ind + 1, seen) for dr, dc in dirs):
                return True
            seen.remove((row, col))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, set()):
                    return True
        return False

        