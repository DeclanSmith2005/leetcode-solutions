class Solution:
    def isValid(self, s: str) -> bool:
        convert = {
        ']' : '[', 
        '}' : '{',  
        ')' : '('
        }
        stack = []
        for l in s:
            if l not in convert:
                stack.append(l)
            elif not stack or stack.pop() != convert[l]:
                    return False
        return not stack