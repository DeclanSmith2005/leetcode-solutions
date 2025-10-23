class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(i) for i in s]
        while len(arr)!=2:
            for i in range(len(arr)-1):
                arr[i] = (arr[i]+ arr[i+1])%10
            del[arr[-1]]
        res = "".join([str(i) for i in arr])
        return res[0] == res[1]
