class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        stack = []
        if len(s) == 0:
            return 0
        i = 1 if s[0] == '-' or s[0] == '+' else 0
        while i < len(s) and s[i] == '0':
            i += 1
        while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
            stack.append(int(s[i]))
            i+=1
        power = 0
        total = 0
        while stack:
            total += stack.pop() * (10**power)
            power += 1
        total = total * (-1) if s[0] == '-' else total
        total = -2**31 if total < -2**31 else total
        return 2**31 - 1 if total > 2**31 - 1 else total
        


        