class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = [None]*32
        for shift in range(32):
            total = 0
            for num in nums:
                num = (num >> shift) & 1
                total += num

            a[31 - shift] = str(total % 3)
        result =  int( "".join(a),2)
        if result >= 2**31:
            result -= 2**32
        return result 