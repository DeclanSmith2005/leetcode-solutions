class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        starts = {} # start - > key
        myMap = {} 

        for k, v in knowledge:
            myMap[k] = v
        l = 0

        for i, char in enumerate(s):
            if char == '(':
                l = i
            if char == ')':
                starts[l] = s[l+1:i]
        
        i = 0 
        res = []

        while i < len(s):
            brick = s[i]
            if i in starts:
                if starts[i] in myMap:
                    brick = myMap[starts[i]]
                else:
                    brick = '?'
                while i < len(s) and s[i] != ')':
                    i+=1
            res.append(brick)
            i += 1

        return "".join(res)