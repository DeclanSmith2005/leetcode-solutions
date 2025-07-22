"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def traverse(row, col, length):
            nonlocal grid
            if length == 1:
                return Node(grid[row][col], True, None, None, None, None)
            check = grid[row][col]
            curr = Node(check, True, None, None, None, None)
            for i in range (row, row+length):
                for k in range(col, col+length): 
                    if grid[i][k] != check:
                        curr.isLeaf = False
                        curr.topLeft = traverse(row, col, length//2)
                        curr.topRight = traverse(row, col+(length//2), length//2)
                        curr.bottomLeft = traverse(row+(length//2), col, length//2)
                        curr.bottomRight = traverse(row+(length//2), col +(length//2), length//2)
            
            return curr
        node = traverse(0,0,len(grid))
        return node


"""
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def traverse(row, col, length):
            nonlocal grid
            if length == 1:
                return Node(grid[row][col], True, None, None, None, None)
            check = grid[row][col]
            curr = Node(check, True, None, None, None, None)
            TL, TR, BL, BR = traverse(row, col, length//2), traverse(row, col+(length//2), length//2), traverse(row+(length//2), col, length//2), traverse(row+(length//2), col +(length//2), length//2)
            if TL.isLeaf and TR.isLeaf and BL.isLeaf and BR.isLeaf and (TL.val == TR.val == BL.val == BR.val):
                return curr
            else:
                curr.isLeaf = False
                curr.bottomLeft = BL
                curr.bottomRight = BR
                curr.topLeft = TL
                curr.topRight= TR
                return curr
        
        node = traverse(0,0,len(grid))
        return node
            

                        



        
            

                        



        