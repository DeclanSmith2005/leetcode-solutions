class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_chars = set(source)
        for char in target:
            if char not in source_chars:
                return -1
        
        left = right = 0
        count = 0

        while right < len(target):
            if source[left] == target[right]:
                right += 1
            left += 1
            if right == len(target) and left < len(source):
                count += 1
            if left == len(source):
                left = 0
                count += 1

        return count