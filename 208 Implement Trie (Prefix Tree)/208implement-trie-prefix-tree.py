class Node():
    def __init__(self, endsHere = False):
        self.next = {}
        self.endsHere = endsHere
    
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for l in word:
            if l in curr.next:
                curr = curr.next[l]
            else:
                curr.next[l] = curr = Node()
        curr.endsHere = True

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word:
            if l not in curr.next:
                return False
            else:
                curr = curr.next[l]
        return curr.endsHere == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for l in prefix:
            if l not in curr.next:
                return False
            else:
                curr = curr.next[l]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)