class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pInd = stack.pop()
                res[pInd] = i - pInd 
            stack.append(i)
        return res