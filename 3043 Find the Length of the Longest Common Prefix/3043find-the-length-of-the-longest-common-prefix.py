class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # store all prefixes of each number in arr1 in a hashmap
        # check all prefixes of each number in arr2 and return the longest one in the hashmap
        seen = set()
        res = 0
        for num in arr1:
            while num > 0:
                seen.add(num)
                num //= 10
        
        for num in arr2:
            while num > 0:
                if num in seen:
                    res = max(res, len(str(num)))
                    break
                num //= 10
        return res
