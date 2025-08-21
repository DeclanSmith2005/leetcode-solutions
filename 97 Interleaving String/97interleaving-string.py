class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        memo = set()
        def recurse(a, b, c):
            nonlocal memo
            if (a, b, c) in memo:
                return False
            if (a>= len(s1) or s1[a] != s3[c]) and (b>= len(s2) or s2[b] != s3[c]):
                    memo.add((a,b,c))
                    return False
        
            temp1, temp2  = a,c
            if a < len(s1) and c < len(s3) and s1[a] == s3[c]:
                a+=1
                c+=1
                if recurse(a, b, c) == True:
                    return True
            if (a == len(s1) and b == len(s2) and c == len(s3)):
                check = True
                return True
            
            a, c = temp1, temp2
            if  b < len(s2) and c < len(s3) and s2[b] == s3[c]:
                b+=1
                c+=1
                if recurse(a, b, c) == True:
                    return True
            if (a == len(s1) and b == len(s2) and c == len(s3)):
                check = True
                return True
            memo.add((a,b,c))
            return False
        return recurse(0,0,0)
            
             