class Solution:
    def reorganizeString(self, s: str) -> str:
        s.lower()
        counts = {char: 0 for char in string.ascii_lowercase}
        for i in s:
            counts[i] += 1
        heap = [(count*(-1), letter) for letter, count in counts.items() if count > 0]
        heapq.heapify(heap)
        res = []
        while heap:
            tmp = ()
            count, letter = heapq.heappop(heap)
            if len(res) > 0 and letter == res[-1]:
                tmp = (count, letter)
                if heap:
                    count, letter = heapq.heappop(heap)
                else:
                    return ""
            res.append(letter)
            if count < -1:
                heapq.heappush(heap, (count+1, letter)) 
            if len(tmp) > 0:
                heapq.heappush(heap, (tmp))
        return "".join(res)
            
            