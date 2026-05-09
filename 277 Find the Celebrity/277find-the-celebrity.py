class Solution:
    def findCelebrity(self, n: int) -> int:
        curr = 0 
            
        for person in range(1,n):
            if knows(curr, person):
                curr = person
            
        for i in range(n):
            if i == curr:
                continue
            if knows(curr, i) or not knows(i, curr):
                return -1

        return curr
       