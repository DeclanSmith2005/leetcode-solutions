class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = [] 
        for i in range( len(expression)):
            if expression[i] != '?' and expression[i] != ':': 
                if len(stack) == 0 and (i == len(expression)-1 or expression[i+1] != '?'):
                    return expression[i]
                elif  len(stack) == 0 and expression[i+1] == '?':
                    stack = [':'] if expression[i] == 'T' else []
            if expression[i] == ':':
                if stack and stack[-1] == '?':
                    stack.pop()
                else:
                    stack.append(expression[i])
            if expression[i] == '?':
                if stack and stack[-1] == ':':
                    stack.pop()
                else:
                    stack.append(expression[i])

