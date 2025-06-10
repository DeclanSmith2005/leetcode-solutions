class Solution:
    def isHappy(self, n: int) -> bool:
        def findPower( num ):
            power = 1
            while 10**power <= num:
                power+=1
            return ( power )

        def getNext(curr):
            pwr = findPower(curr)
            nextNum = 0
            for i in range(pwr):
                temp = curr
                temp = (temp // 10**i) % 10
                nextNum += (temp**2)
            return nextNum
        
        fast = n
        slow = n

        while True:
            fast = getNext(getNext(fast))
            slow = getNext(slow)
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
  