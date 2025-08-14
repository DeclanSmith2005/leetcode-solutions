class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashBank = set(wordList)
        neighbors = deque([beginWord])
        endNeighbors = deque([endWord])
        seen = set()
        endSeen = set()
        steps = 0
        if endWord not in hashBank:
            return 0
        def findNeighbors(word, side):
            retList = []
            for letter in range(len(word)):
                temp = list(word)
                for alteration in string.ascii_lowercase:
                    if alteration == temp[letter]:
                        continue
                    temp[letter] = alteration
                    strTemp = ''.join(temp)
                    if side == 0:
                        if strTemp in hashBank and strTemp not in seen:
                            retList.append(strTemp)
                    else:
                        if strTemp in hashBank and strTemp not in endSeen:
                            retList.append(strTemp)
            return retList
        
        count =0 
        while len(neighbors) != 0:
            for i in range(len(neighbors)):
                curr = neighbors.popleft()
                seen.add(curr)
                neighbors.extend(findNeighbors(curr, 0))
            if not seen.isdisjoint(endSeen):
                return count 
            count +=1 
            for i in range(len(endNeighbors)):
                curr = endNeighbors.popleft()
                endSeen.add(curr)
                endNeighbors.extend(findNeighbors(curr, 1))
            if not seen.isdisjoint(endSeen):
                return count 
            count +=1
            
        return 0