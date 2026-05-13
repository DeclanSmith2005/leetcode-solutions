"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldMap = {None:None}
        newMap = {None:None}
        oldPtr = head
        newPtr = newHead = Node(0)
        i = 0
        while oldPtr:
            newPtr.next = Node(oldPtr.val)
            oldMap[oldPtr] = i
            newMap[i] = newPtr.next
            oldPtr= oldPtr.next
            newPtr = newPtr.next
            i+=1
        
        oldPtr = head
        newPtr = newHead.next
        
        while oldPtr:
            newPtr.random = newMap[oldMap[oldPtr.random]]
            oldPtr, newPtr = oldPtr.next, newPtr.next
        return newHead.next
            