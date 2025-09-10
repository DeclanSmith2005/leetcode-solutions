class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [0]*len(isConnected)
        rank = [1 for i in range(len(isConnected))]
        for i in range(len(parents)):
            parents[i] = i
        for row in range(len(isConnected)):
            for col in range(row, len(isConnected[0])):
                if isConnected[row][col] == 1:
                    parent1 = parents[row]
                    parent2 = parents[col]
                    while parents[parent1] != parent1:
                        parent1 = parents[parent1]
                    while parents[parent2] != parent2:
                        parent2 = parents[parent2]
                    if parent1 == parent2:
                        continue
                    if rank[parent1] > rank[parent2]:
                        parents[parent2] = parents[parent1]
                        rank[parent1] += rank[parent2]
                        rank[parent2] = 0
                    else:
                        parents[parent1] = parents[parent2]
                        rank[parent2] == rank[parent1]
                        rank[parent1] = 0
        numProvinces = 0
        for i in rank:
            if i > 0:
                numProvinces += 1
        return numProvinces


                    
