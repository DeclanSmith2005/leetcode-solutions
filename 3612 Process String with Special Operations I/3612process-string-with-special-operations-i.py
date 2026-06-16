class Solution:
    def processStr(self, s: str) -> str:
        resString =  []
        for l in s:
            if l == '*': 
                if resString:
                    resString.pop()
            elif l == '#':
                resString = resString + resString
            elif l == '%':
                resString = resString[::-1]
            else:
                resString.append(l)
        return "".join(resString)