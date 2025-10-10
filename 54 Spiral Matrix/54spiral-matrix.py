class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len (matrix[0])
        LB = 0
        UB = 0
        retList = []
        total =0 
        count = 0
        for i in matrix:
            total+= len(i)

        while count<total:
            #left->right
            if LB == n:
                retList.append(matrix[UB][LB])
                count+=1
            else:
                for i in range(LB, n):
                    retList.append(matrix[UB][i])
                    count+=1
            n-=1
            UB+=1
            if (total==count):
                return retList

            #top-> bottom
            if UB == m:
                retList.append(matrix[UB][n])
                count+=1
            else:
                for i in range (UB, m):
                    retList.append(matrix[i][n])
                    count+=1
            m-=1
            
            if (total==count):
                return retList

            #right-> left
            if n-1 ==LB:
                retList.append(matrix[m][LB])
                count+=1
            else:
                for i in range (n-1,LB-1,-1):
                    retList.append(matrix[m][i])
                    count+=1
            
            if (total==count):
                return retList

            # bottom -> top
            if m-1 == UB:
                retList.append(matrix[m-1][LB])
                count+=1
            else:
                for i in range (m-1, UB-1, -1):
                    retList.append(matrix[i][LB])
                    count+=1
            LB+=1
            if (total==count):
                return retList


        