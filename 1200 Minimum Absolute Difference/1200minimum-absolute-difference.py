class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDif = arr[1]- arr[0]
        curr = [] 
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < minDif:
                curr = [[arr[i], arr[i+1]]]
                minDif = diff
            elif diff == minDif:
                curr += [(arr[i], arr[i+1])]
        return curr