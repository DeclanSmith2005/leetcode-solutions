class Solution:
    def sumAndMultiply(self, n: int) -> int:
        tmp = str(n)
        x= []
        for i in tmp:
            if i != '0':
                x.append(i)
        x = int("".join(x)) if len("".join(x)) > 0 else 0 
        summ = sum(int(i) for i in str(x))
        return x * summ
