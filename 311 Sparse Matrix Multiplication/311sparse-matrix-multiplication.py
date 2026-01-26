class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        nonZero1 = []
        nonZero2= []
        for row in range(len(mat1)):
            curr = []
            for col in range(len(mat1[0])):
                if mat1[row][col] != 0:
                    curr.append([mat1[row][col], col])
            nonZero1.append(curr)

        for row in range(len(mat2)):
            curr = []
            for col in range(len(mat2[0])):
                if mat2[row][col] != 0:
                    curr.append([mat2[row][col], col])
            nonZero2.append(curr)
        res = [[0]*len(mat2[0]) for i in range(len(mat1))]

        for row in range(len(nonZero1)):
            for val1, col1 in nonZero1[row]:
                for val2, col2 in nonZero2[col1]:
                    res[row][col2] += val1 * val2
        return res

