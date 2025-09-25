class Solution:
    def partition(self, s: str) -> List[List[str]]:
        neighbors = {} 
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left in neighbors:
                    neighbors[left].append(right+1)
                else:
                    neighbors[left] = [right+1]
                left -=1
                right +=1 

            #check even length palindromes
            left, right = i-1, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left in neighbors:
                    neighbors[left].append(right+1)
                else:
                    neighbors[left] = [right+1]
                left -=1
                right +=1 

        retList = []
        def recurse(index, curr):
            if index == len(s):
                retList.append(curr.copy())
                return
            for neighbor in neighbors[index]:
                curr.append(s[index:neighbor])
                recurse(neighbor, curr)
                curr.pop()
        
        curr = []
        recurse(0, curr)

        return retList



