# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        memo = {}
        longest = 0
        def zigZag(dir, node, depth):
            if node == None:
                return depth
            depth +=1
            if node in memo:
                return depth + memo[node][0] if dir == 0 else depth + memo[node][1]
            if dir == 1:
                return zigZag(0, node.right, depth)
            else:
                return zigZag(1, node.left, depth)

        def postOrder(node):
            nonlocal longest
            if not node:
                return
            postOrder(node.left)
            postOrder(node.right)
            right = zigZag(0, node.right, 0)
            left = zigZag(1, node.left, 0)
            memo[node] = (left, right)
            longest = max(left, right, longest)
                    
        postOrder(root)
        return longest
            
            
        
            
                