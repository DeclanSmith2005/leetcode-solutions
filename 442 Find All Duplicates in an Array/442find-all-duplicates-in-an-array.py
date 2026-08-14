class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Step 1: Put each number in its correct place (e.g., 3 goes to index 2)
        i = 0
        while i < len(nums):
            # The correct index for the number nums[i]
            correct_idx = nums[i] - 1
            
            # If the number is not already at its correct index, swap it
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # Only move forward when the current spot has the right number 
                # OR a duplicate we can't move
                i += 1
                
        # Step 2: Any number that didn't end up at its correct index is a duplicate
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
                
        return res