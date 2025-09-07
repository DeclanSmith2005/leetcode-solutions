class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        returnString = []
        stack = 0
        curr = []
        for string in source:
            i = 0
            double = False
            while i < len(string):
                if i < len(string)-2:
                    if string[i] == "/" and string[i+1] == "*" and string [i+2] == "/":
                        if stack ==1:
                            stack = 0
                            i+=3
                            continue
                        elif double == False:
                            stack = 1
                            i+=2
                            continue

                if i < len(string)-1:
                    if string[i] == "/" and string[i+1] == "*" and double == False:
                        stack=1
                        i+=1
                        continue
                    if string[i] == "*" and string[i+1] == "/" and stack == 1:
                        stack = 0
                        i+=2
                        continue
                    if string[i] == "/" and string[i+1] == "/" and stack == 0:
                        double = True
                if stack == 0 and double == False:
                    curr.append(string[i])
                i+=1
            if curr != [] and stack == 0:
                returnString.append("".join(curr))
                curr = []
        return returnString
                