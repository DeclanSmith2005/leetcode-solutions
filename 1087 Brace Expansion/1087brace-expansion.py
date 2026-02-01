class Solution:
    def expand(self, s: str) -> List[str]:
        res = [[]]
        curr= []
        inBraces = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == ',':
                continue
            if s[i] == '}':
                curr = []
                inBraces = True
            elif s[i] == '{':
                res = deepcopy(curr)
                inBraces = False
            else:
                if inBraces:
                    for k in res:
                        curr.append(deepcopy(k))
                        curr[-1].append(s[i])
                else:
                    for k in res:
                        k.append(s[i])
        return sorted(["".join(reversed(i)) for i in res])
                

