class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; currNum = 0; currString = []
        for char in s:
            if char == '[':
                stack.append(currNum)
                stack.append(currString)
                currNum = 0
                currString = []
            elif char == ']':
                currString = stack.pop() + (stack.pop() * currString)
                prevString = currString
            elif char.isalpha():
                currString.append(char)
            else:
                currNum = currNum*10 +int(char)
        return "".join(currString)
                
            
