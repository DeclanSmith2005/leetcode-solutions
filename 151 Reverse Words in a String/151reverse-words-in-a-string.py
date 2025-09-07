class Solution:
    def reverseWords(self, s: str) -> str:
        returnString = deque([])
        for i in s.split():
            returnString.appendleft(i)
        return " ".join(returnString)
