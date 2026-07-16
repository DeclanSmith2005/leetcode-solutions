class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = [nums[0] for _ in range(len(nums))]
        pGCD = mx[:]

        def GCD(a, b):
            while b:
                tmp = b
                b = a % b
                a = tmp
            return a


        for i in range(1, len(mx)):
            mx[i] = max(mx[i-1], nums[i])
            pGCD[i] = GCD(nums[i], mx[i])
        pGCD.sort()
        res = 0
        for i in range(len(pGCD)//2):
            res += GCD(pGCD[i], pGCD[-i-1])

        return res

        

