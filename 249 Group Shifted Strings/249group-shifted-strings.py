class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in range(len(strings)):
            curr= []
            for i in range(len(strings[s])-1):
                curr.append((ord(strings[s][i]) - ord(strings[s][i+1]))%26)
            groups[tuple(curr)].append(s)
        res = []
        for key, val in groups.items():
            res.append([])
            for s in val:
                res[-1].append(strings[s][:])
        return res

