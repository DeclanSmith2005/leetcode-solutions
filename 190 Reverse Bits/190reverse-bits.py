class Solution:
    def reverseBits(self, n: int) -> int:
        binString = bin(n)[2:]
        diff = 32 - len(binString)
        padding = "0"*diff
        binString = padding + binString
        reversedString = 32*[""]
        ind = 0 
        for i in range(31,0, -1):
            reversedString[i] = binString[ind]
            ind +=1
        return int("".join(reversedString),2)
