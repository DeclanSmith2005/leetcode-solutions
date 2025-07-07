# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        if root == None:
            return []
        retList = []
        one = True
        while q:
            curr = []
            if one:
                for i in range(len(q)):
                    node = q.popleft()
                    curr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            else:
                for i in range(len(q)):
                    node = q.pop()
                    curr.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            one = not one
            retList.append(curr)
        return retList
        