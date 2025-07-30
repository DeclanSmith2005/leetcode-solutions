class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = zip(capital, profits)
        pairs = sorted(pairs)
        heap = []
        j = 0
        for i in range(k):
            while j < len(pairs) and pairs[j][0] <= w:
                heapq.heappush(heap, -pairs[j][1])
                j+=1
            if len(heap) != 0:
                w+= -heapq.heappop(heap)
        return w

           


"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mappings = {}
        money = w
        for i in range(len(profits)):
            if capital[i] in mappings:
                heapq.heappush(mappings[capital[i]], -profits[i])
            else:
                mappings[capital[i]] = [-profits[i]]
        i= 0
        while i < k:
            if len(mappings) == 0:
                return money
            if money in mappings:
                temp = money
                money += -heapq.heappop(mappings[money])
                if mappings[temp] == []:
                    del mappings[temp]
            else:
                temp = money
                while temp not in mappings:
                    temp-=1
                    if temp < 0:
                        return money
                money+= -heapq.heappop(mappings[temp])
                if mappings[temp] == []:
                    del mappings[temp]
            i+=1
        return money

        
"""


        