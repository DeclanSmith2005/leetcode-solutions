class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def columnIsValid(col, startInd, endInd, board):
            seen = set()
            for i in range(startInd, endInd):
                temp = board[i][col]
                if temp != ".":
                    if temp in seen:
                        return [False]
                    seen.add(temp)
            myList = [True]
            myList.append(seen)
            return myList


        def rowIsValid(row, startInd, endInd, board):
            seen = set()
            for i in range(startInd, endInd):
                temp = board[row][i]
                if temp != ".":
                    if temp in seen:
                        return [False]
                    seen.add(temp)
            myList = [True]
            myList.append(seen)
            return myList

        def squareIsValid(row, col, board):
            seen = set()
            for i in range(3):
                temp = rowIsValid(row+i, col, col+3, board)
                if temp[0] == False:
                        return [False]
                else:
                    if set(temp[1]).isdisjoint(seen):
                        seen = set(temp[1]).union(seen)
                    else:
                        return False
            return True

        i = 0
        while i< 9 and columnIsValid(i, 0, 9, board)[0] == True:
            i+=1
        if i!= 9:
            return False

        #########################################
        i = 0 
        while i<9 and rowIsValid(i, 0, 9, board)[0] == True:
            i+=1
        if i!= 9:
            return False
        
        indicies = [0,3,6]

        for i in indicies:
            for k in indicies:
                if squareIsValid(i, k, board) == False:
                    return False
            
        return True


        
    