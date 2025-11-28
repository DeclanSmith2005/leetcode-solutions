class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        vowelsUpper = [c.upper() for c in vowels]

        stack = []
        usedPositions = set()
        for i in range(len(s)):
            if s[i] in vowelsUpper or s[i] in vowels:
                stack.append(s[i])
                usedPositions.add(i)
        newString = []
        for i in range(len(s)):
            if i in usedPositions:
                newString.append(stack.pop())
            else:
                newString.append(s[i])
        return "".join(newString)


