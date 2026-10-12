class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            curr = "".join(sorted([c for c in s]))
            groups[curr].append(s)
        return list(groups.values())

