class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        res= []
        for i in range(max(len(A), len(B))):
            if i < len(A):
                setA.add(A[i])
            if i < len(B):
                setB.add(B[i])
            res.append(len(setA & setB))
        return res