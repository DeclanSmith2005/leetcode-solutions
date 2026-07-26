class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
            
        buckets = {}
        # Bucket size is valueDiff + 1 to handle ranges (e.g., valueDiff of 2 means size 3: 0,1,2)
        bucket_size = valueDiff + 1 
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            
            # 1. Check if we already have a number in the exact same bucket
            if bucket_id in buckets:
                return True
                
            # 2. Check the adjacent left bucket
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # 3. Check the adjacent right bucket
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
                
            # Put the current number in its bucket
            buckets[bucket_id] = num
            
            # Maintain the sliding window size of `indexDiff`
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]
                
        return False
