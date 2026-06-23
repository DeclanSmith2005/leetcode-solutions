class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr) == 1:
                return arr
            if len(arr) == 2:
                return arr if arr[0] <= arr[1] else [arr[1], arr[0]]
            a = merge([arr[i] for i in range(len(arr)//2)]) 
            b = merge([arr[i] for i in range((len(arr)//2), len(arr))])
            ans = []
            l, r = 0, 0
            while l < len(a) and r < len(b):
                if a[l] < b[r]:
                    ans.append(a[l])
                    l += 1
                else:
                    ans.append(b[r])
                    r += 1
            ans.extend(b[r:len(b)] if l == len(a) else a[l:len(a)])
            return ans
            
        return merge(nums)
            