class StringIterator:

    def __init__(self, compressedString: str):
        self.ind = 0
        self.string = compressedString
        self.curr = ""
        

    def next(self) -> str:
        if self.hasNext():
            if len(self.curr) == 0:
                letter = self.string[self.ind]
                self.ind+=1
                og = self.ind
                while self.ind+1 < len(self.string) and self.string[self.ind+1].isdigit():
                    self.ind+=1
                self.curr = letter * int(self.string[og:self.ind+1])
                self.ind += 1
            res = self.curr[0]
            self.curr = self.curr[1:]
            return res
        return ' '
        

    def hasNext(self) -> bool:
        return self.ind < len(self.string) or len(self.curr) > 0



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()