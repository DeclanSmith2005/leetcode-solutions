# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.i = 0
        self.inO(root)

    def next(self) -> int:
        ans = self.res[self.i]
        self.i+=1
        return ans

    def hasNext(self) -> bool:
        return self.i < len(self.res)
        
    def inO(self, n):
        if not n:
            return None
        self.inO(n.left)
        self.res.append(n.val)
        self.inO(n.right)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()