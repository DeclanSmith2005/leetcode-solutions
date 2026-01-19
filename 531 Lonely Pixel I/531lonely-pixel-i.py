class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        perRow = [0 for r in range(len(picture))]
        perCol = [0 for c in range(len(picture[0]))]
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B':
                    perRow[row] += 1
                    perCol[col] += 1
        count = 0 
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B' and perRow[row] == 1 and perCol[col] == 1:
                    count += 1
        return count

        