class Solution:
    def compress(self, chars: List[str]) -> int:
        l = s = total = 0
        for e in range(len(chars)+1):
            if  e == len(chars) or chars[e] != chars[s]:
                diff = e-s
                chars[l] = chars[s]
                total , l = total +1, l +1  
                if diff > 1:
                    temp = str(diff)
                    for i in range(len(temp)):
                        chars[l] = temp[i]
                        l += 1
                        total += 1
                s = e
        chars[:] = chars[:total]

            
               

                

            