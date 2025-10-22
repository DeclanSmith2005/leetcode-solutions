class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            nums = queryIP.split(".")
            if len(nums) == 4:
                for num in nums:
                    for digit in num:
                        if not digit.isdigit():
                            return "Neither"
                    if len(num) == 0 or int(num) not in range(0, 256): 
                        return "Neither"
                    if len(num) > 1 and int(num) == int(num[1:]):
                        return "Neither"
                return "IPv4"
            else:
                return "Neither"
        elif ':' in queryIP:
            nums = queryIP.split(":")
            if len(nums) == 8:
                for num in nums:
                    if len(num) > 4 or len(num) ==0:
                        return "Neither"
                    for digit in num:
                        if not( digit.isdigit() or ord('a') <= ord(digit) <= ord('f') or ord('A') <= ord(digit) <= ord('F')): 
                            return "Neither"
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"

