class Solution:
    # determine the full list of differences
    # search for a guy that has just 1
    # search for a guy that matches that description, but has 1 more, 
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        hashBank = set(bank)
        changes = ["A", "C", "G", "T"]
        neighbors = deque([startGene])
        seen = set()
        steps = 0
        if bank == []:
            return -1
        def findNeighbors(gene):
            nonlocal neighbors
            for letter in range(len(gene)):
                temp = list(gene)
                for alteration in changes:
                    if alteration == temp[letter]:
                        continue
                    temp[letter] = alteration
                    strTemp = ''.join(temp)
                    if strTemp in hashBank and strTemp not in seen:
                        neighbors.append(strTemp)
                        if strTemp == endGene:
                            return True
            return False 
        count = 1 
        while len(neighbors) != 0:
            for i in range(len(neighbors)):
                curr = neighbors.popleft()
                seen.add(curr)
                if findNeighbors(curr) == True:
                    return count
            count +=1
        return -1
            



