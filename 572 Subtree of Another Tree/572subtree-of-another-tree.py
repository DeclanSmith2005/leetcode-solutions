# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRootQ = deque([subRoot])
        srNodes = []
        while subRootQ:
            curr = subRootQ.pop()
            if curr:
                subRootQ.appendleft(curr.left)
                subRootQ.appendleft(curr.right)
                srNodes.append(curr.val)
            else:
                srNodes.append(None)



        def preOrder(node):
            if node == None:
                return False
            if preOrder(node.left):
                return True
            check= []
            q = deque([node])
            i = 0
            while q and len(check) < len(srNodes):
                curr = q.pop()
                if curr:
                    q.appendleft(curr.left)
                    q.appendleft(curr.right)
                    check.append(curr.val)
                else:
                    check.append(None)
                if check[i] != srNodes[i]:
                    break
                i+=1
            return True if len(q) == 0 and len(check) == len(srNodes) and check[-1] == srNodes[-1] else preOrder(node.right)
        
        return preOrder(root)

            