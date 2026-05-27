class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        good = set()
        bad = set()
        maybe = set()
        for l in word:
            if l.lower() == l:
                maybe.add(l.lower())
                if l in good:
                    bad.add(l.lower())
            if l.upper() == l:
                if l.lower() in maybe:
                    good.add(l.lower())
                else:
                    bad.add(l.lower())
        return len(good - bad)
        
                