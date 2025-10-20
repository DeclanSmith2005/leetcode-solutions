class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            x, y = 0, 0
            if len(words[i+1]) < len(words[i]) and words[i+1] == words[i][:len(words[i+1])]:
                return ""
            while words[i][x] == words[i+1][y] and (x < len(words[i])-1 or y < len(words[i+1])-1):
                if x < len(words[i]) - 1:
                    x += 1
                if y < len(words[i+1]) - 1:
                    y += 1
        
            if words[i][x] != words[i+1][y]:
                adj[words[i][x]].add(words[i+1][y])

        visiting = set()
        visited = set()
        res = []
        def dfs(ch):
            if ch in visited:
                return True
            elif ch in visiting:
                return False
            visiting.add(ch)
            for next_ch in adj[ch]:
                if not dfs(next_ch):
                    return False
            res.append(ch)
            visiting.remove(ch)
            visited.add(ch)
            return True
        
        for c in adj.keys():
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)