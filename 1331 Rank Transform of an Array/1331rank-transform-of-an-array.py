class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        check = sorted(arr)
        ranks = {}
        rank = 1
        for i in range(len(arr)):
            ranks[check[i]] = rank
            if i < len(arr)-1 and check[i] < check[i+1]:
                rank += 1
            
        return [ranks[num] for num in arr]