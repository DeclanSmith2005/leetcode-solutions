class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}
        for i in magazine:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        for i in ransomNote:
            if i not in seen or seen[i] == 0:
                return False
            seen[i] -=1
        return True