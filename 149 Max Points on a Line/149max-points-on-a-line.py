class Solution:

    # create a relational graph of all the points within 1 step of each point
    # depth first search along line of each adjacent node
    # add that line as y = mx+ B to set of looked at lines
    # greatest num of nodes
    # do this for each node for each of its immediate neighbors
    # at each one if the line is already in the set break. 
    # search from X min to X max and Ymin to Ymax
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_count = 0
        for i in range(len(points)):
            slopes = {}
            same_point = 1
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    same_point += 1
                    continue
                g = gcd(dx, dy)
                slope = (dy // g, dx // g)
                slopes[slope] = slopes.get(slope, 0) + 1
            max_count = max(max_count, same_point + max(slopes.values(), default=0))
        return max_count

        