class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for i in range(len(arr)):
            occurences[arr[i]] = occurences.get(arr[i], 0) + 1
        keys, vals = occurences.keys(), set(occurences.values())
        return len(keys) == len(vals)        