class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        check = set(arr)
        for i in range(len(arr)):
            if arr[i] + 1 in check:
                counts[arr[i]] += 1
        return sum(counts.values())