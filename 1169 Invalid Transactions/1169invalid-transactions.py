class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        check  = {}
        frauds = []
        added = set()
        for i in range(len(transactions)):
            curr = transactions[i].split(",")
            curr [1], curr[2], = int(curr[1]), int(curr[2])
            if (curr[2]) > 1000:
                frauds.append(transactions[i])
                added.add(i)
            if curr[0] in check:
                left, right = 0, len(check[curr[0]])
                while left < right:
                    mid  = (left + right) //2 
                    if (check[curr[0]][mid][0]) >= (curr[1]):
                        right = mid
                    else:
                        left = mid+1
                checkIndicies = []
                temp = left -1 
                while temp > -1 and temp < len(check[curr[0]]) and (check[curr[0]][temp][0]) >= (curr[1]) - 60:
                    checkIndicies.append(temp)
                    temp -=1
                temp = left 
                while temp > -1 and temp < len(check[curr[0]]) and (check[curr[0]][temp][0]) <= (curr[1]) +60:
                    checkIndicies.append(temp)
                    temp +=1
                for index in checkIndicies:
                    if check[curr[0]][index][1] != curr[3]:
                        if i not in added:
                            frauds.append(transactions[i])
                            added.add(i)
                        if check[curr[0]][index][2] not in added:
                            frauds.append(transactions[check[curr[0]][index][2]])
                            added.add(check[curr[0]][index][2])
                check[curr[0]].insert(left, [curr[1], curr[3], i])
            else:
                check[curr[0]] = [[int(curr[1]), (curr[3]), i]]
        return frauds

