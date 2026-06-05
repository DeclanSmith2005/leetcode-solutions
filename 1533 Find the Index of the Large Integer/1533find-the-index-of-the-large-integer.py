class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if (right - left + 1) % 2 == 0:
                # even length
                res = reader.compareSub(left, mid, mid + 1, right)
                if res == 1:
                    right = mid
                else:
                    left = mid + 1
            else:
                # odd length → skip middle
                res = reader.compareSub(left, mid - 1, mid + 1, right)
                if res == 0:
                    return mid
                elif res == 1:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return left
