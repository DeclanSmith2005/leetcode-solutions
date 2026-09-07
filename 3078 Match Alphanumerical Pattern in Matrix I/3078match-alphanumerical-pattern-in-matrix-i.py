class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        n = len(board)
        m = len(board[0])
        for i in range(n - len(pattern) + 1):
            for j in range(m - len(pattern[0]) + 1):
                intToCh = {} #board int: pattern ch
                chToInt = {} #board pattern ch: int
                matching = True
                for dx in range(len(pattern)):
                    if not matching: break
                    for dy in range(len(pattern[0])):
                        nx = i + dx
                        ny = j + dy
                        number = board[nx][ny]
                        patternCh = pattern[dx][dy]
                        if str.isnumeric(patternCh):
                            if int(patternCh) == number:
                                continue
                            else:
                                matching = False
                                break
                        if number not in intToCh and patternCh not in chToInt:
                            intToCh[number] = patternCh
                            chToInt[patternCh] = number
                        elif number in intToCh and patternCh in chToInt and intToCh[number] == patternCh and chToInt[patternCh] == number:
                            continue
                        else:
                            matching = False
                            break

                if matching:
                    return [i, j]
        return [-1, -1]