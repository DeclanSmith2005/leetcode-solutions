class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res= []
        for num in arr:
            binary = bin(num)[2:]
            count = sum([0 if binary[i] == '0' else 1 for i in range(len(binary))])
            res.append((count, num))
        return[i[1] for i in sorted(res)]
            