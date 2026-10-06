class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversedNum= 0
        tmpx = x
        while tmpx:
            reversedNum = (reversedNum*10 )+  tmpx%10
            tmpx //= 10
        return reversedNum == x