class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.dict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        one_indexes = self.dict[word1]
        two_indexes = self.dict[word2]
        
        j = 0
        sort = []
        for i in range(len(one_indexes)):
            while j < len(two_indexes) and one_indexes[i] >= two_indexes[j]:
                sort.append((2, two_indexes[j]))
                j += 1
            sort.append((1, one_indexes[i]))
        while j < len(two_indexes):
            sort.append((2, two_indexes[j]))
            j += 1
        
        res = float('inf')
        for i in range(len(sort)-1):
            if sort[i][0] != sort[i+1][0]:
                res = min(res, sort[i+1][1] - sort[i][1])
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)