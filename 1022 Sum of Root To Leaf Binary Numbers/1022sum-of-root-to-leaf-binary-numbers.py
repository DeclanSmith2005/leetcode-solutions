# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        curr = []
        total = 0
        def inOrder(node, total):
            nonlocal curr
            if not node:
                return 0
            curr.append(str(node.val))
            if not (node.left or node.right):
                if curr:
                    total += int("".join(curr), 2)
                    curr.pop()
                return total
            tmp = total
            tmp += inOrder(node.left, total)
            tmp += inOrder(node.right, total)
            curr.pop()
            return tmp

        return inOrder(root, 0)
         