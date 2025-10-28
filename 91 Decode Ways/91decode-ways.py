class Solution:
    def numDecodings(self, s: str) -> int:
        codes =0
        memo = {}
        def backTrack(encoding, i):
            nonlocal codes
            if i in memo:
                codes += memo[i]
                return
            start, startCodes = i , codes
            if i == len(s):
                codes +=1
                return
            if s[i] == '0':
                memo[i] = 0
                return
            if i < len(s):
                encoding.append([s[i]])
                backTrack(encoding, i +1)
                encoding.pop()
            if i < len(s)-1:
                if int("".join([s[i], s[i+1]])) > 26:
                    return
                encoding.append([s[i], s[i+1]])
                backTrack(encoding, i+2)
                encoding.pop()

            memo[start] = codes - startCodes
                
        backTrack([], 0)
        return codes



