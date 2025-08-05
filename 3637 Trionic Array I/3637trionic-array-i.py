class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        flips =0 
        counts = []
        while i< len(nums)-1:
            count = 0
            while i< len(nums)-1 and (nums[i+1] - nums[i]) > 0:
                i+=1
                count+=1
            print (i == len(nums)-1, nums[i-1] - nums[i] > 0, flips == 2)
            if i == len(nums)-1 and nums[i] - nums[i-1] > 0 and flips == 2:
                return True
            flips+=1
            print(count)
            if flips > 2:
                return False
            if count < 1:
                return False
            counts.append(count)
            count = 0
            
            
            while i< len(nums)-1 and (nums[i+1] - nums[i]) < 0:
                i+=1
                count+=1
            flips+=1
            print (count)
            if flips > 2:
                return False
            if count < 1:
                return False
            counts.append(count)
        if len(counts) ==3:
            if counts[0] == counts[1] == counts[2] == 1:
                return False
        else:
            return False
        return True