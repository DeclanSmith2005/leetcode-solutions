class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indexes = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                indexes.append((1, i))
            elif wordsDict[i] == word2:
                indexes.append((2, i))
        
        res = float('inf')
        for i in range(len(indexes)-1):

            if word1 != word2 and indexes[i][0] == indexes[i+1][0]:
                continue
            
            res = min(res, indexes[i+1][1] - indexes[i][1])
        return res

        
        

