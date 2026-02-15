class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar = defaultdict(set)
        for a , b in similarPairs:
            similar[a].update((a, b))
            similar[b].update((a, b))
        if len(sentence1) != len(sentence2):
            return False
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence1[i] not in similar or sentence2[i] not in similar[sentence1[i]]:
                return False
        return True
        