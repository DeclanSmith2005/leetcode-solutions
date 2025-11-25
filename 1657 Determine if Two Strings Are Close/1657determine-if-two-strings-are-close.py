class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ones = defaultdict(int)
        twos = defaultdict(int)
        for i in word1:
            ones[i] +=1
        for i in word2:
            twos[i] += 1
        return sorted(ones.values()) == sorted(twos.values()) and ones.keys() == twos.keys()
        
                
            


