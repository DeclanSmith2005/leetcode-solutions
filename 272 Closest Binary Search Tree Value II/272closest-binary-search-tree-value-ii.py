# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        closest = []
        def inOrder(node):
            nonlocal closest
            if not node:
                return
            inOrder(node.left)
            if not closest:
                heapq.heappush(closest, ((-1)*abs(target- node.val), node.val))
            else:
                if abs(target- node.val) < (-1) * closest[0][0] or len(closest) < k:
                    if len(closest) == k:
                        heapq.heappop(closest)
                    heapq.heappush(closest, ((-1)*abs(target- node.val), node.val))
            inOrder(node.right)
        inOrder(root)
        return [i[1] for i in closest]
