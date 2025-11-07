class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = alt = 0
        for i in gain:
            alt +=i
            highest = max(highest,alt)
        return highest