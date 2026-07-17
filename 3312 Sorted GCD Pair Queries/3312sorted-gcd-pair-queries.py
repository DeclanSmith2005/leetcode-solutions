from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        
        # 1. Count the frequency of every number in nums
        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1
            
        # cnt[g] will store the EXACT number of pairs with GCD == g
        cnt = [0] * (M + 1)
        
        # 2. Go backwards from the largest possible GCD down to 1
        for g in range(M, 0, -1):
            # Count how many numbers in nums are multiples of g
            multiples_count = 0
            for k in range(g, M + 1, g):
                multiples_count += freq[k]
            
            # Calculate how many total pairs we can make from these multiples
            pairs = multiples_count * (multiples_count - 1) // 2
            
            # 3. Subtract pairs that actually have a strictly larger multiple as their GCD
            # (e.g., if g=2, we subtract the pairs that had a GCD of 4, 6, 8...)
            for k in range(2 * g, M + 1, g):
                pairs -= cnt[k]
                
            cnt[g] = pairs
            
        # 4. Create a prefix sum array to quickly answer queries
        # prefix[i] will be the total number of pairs with a GCD <= i
        prefix = [0] * (M + 1)
        for i in range(1, M + 1):
            prefix[i] = prefix[i - 1] + cnt[i]
            
        # 5. For each query (which asks for the q-th 0-indexed pair), 
        # use binary search to instantly find which GCD bucket it falls into.
        return [bisect_right(prefix, q) for q in queries]