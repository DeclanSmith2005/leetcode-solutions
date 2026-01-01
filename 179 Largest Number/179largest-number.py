class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            m = (len(a)+ len(b))
            for i in range(m):
                if a[i%len(a)] != b[i%len(b)]:
                    return 1 if a[i%len(a)] < b[i%len(b)] else -1
            return 0
        nums = sorted([str (i) for i in nums], key= cmp_to_key(compare))
        return str(int("".join(nums)))
        

