class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        n, children = len(pid), defaultdict(list)
        for i in range(n):
            children[ppid[i]].append(pid[i])
        res= []
        def dfs(idt):
            nonlocal res
            for ch in children[idt]:
                dfs(ch)
            res.append(idt)
        dfs(kill)
        return res
