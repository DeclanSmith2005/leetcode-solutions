class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        operators  = {"+", "-", "*", "/"}
        for i in tokens:
            if i in operators:
                result = 0
                num1 = myStack.pop()
                num2 = myStack.pop()
                if i == "+":
                    result = int(num1)+int(num2)
                elif i == "-":
                    result = int (num2)-int(num1)
                elif i == "/":
                    result = int(num2)/int(num1)
                elif i == "*":
                    result = int(num2)*int(num1)
                myStack.append(result)
            else:
                myStack.append(i)
        return int(myStack.pop())


            