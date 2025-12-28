class TNode():
    count = 3
    res = []
    used = set()
    def __init__(self):
        self.children = {}
        self.end = False
    
    def add(self, word):
        if len(word) == 0:
            self.end = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = TNode()
        self.children[word[0]].add(word[1:])
        
    
    def search(self, word, curr):
        if len(word) > 0:
            curr.append(word[0])
            if word[0] in self.children:
                self.children[word[0]].search(word[1:], curr)
            else:
                return
        else:
            if TNode.count == 0:
                return
            if len(self.children) == 0:
                TNode.count -= 1
                TNode.res.append("".join(curr))
                TNode.used.add("".join(curr))
            for char in string.ascii_lowercase:
                if self.end and TNode.count> 0 and "".join(curr) not in TNode.used:
                    TNode.count -=1
                    TNode.res.append("".join(curr))
                    TNode.used.add("".join(curr))
                if char in self.children:
                    curr.append(char)
                    self.children[char].search("", curr)
                    curr.pop()

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root= TNode()
        out = []
        for word in products:
            root.add(word)
        for l in range(1, len(searchWord)+1):
            word = searchWord[:l]
            TNode.count = 3
            root.search(word, [])
            out.append(TNode.res)
            TNode.res = []
            TNode.used = set()
        return out


