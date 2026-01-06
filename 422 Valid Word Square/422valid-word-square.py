class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        longs= []
        for i in range(len(words)):
            curr = []
            for word in words:
                if i < len(word):
                    curr.append(word[i])
                else:
                    curr.append(' ')
            longs.append("".join(curr))
            curr = []
        for i in range(len(longs)):
            if longs[i].rstrip() != words[i]:
                return False
        return True