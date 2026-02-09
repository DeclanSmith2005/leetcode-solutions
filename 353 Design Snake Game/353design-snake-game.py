class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake =deque([(0,0)])
        self.food = food[::-1]
        self.width, self.height = width, height
        self.dirs = {"R": (0,1), "L": (0,-1), "U":(-1,0), "D":(1,0)}
        self.occupied = set([(0,0)])

    def move(self, direction: str) -> int:
        dr, dc = self.dirs[direction]
        row, col = self.snake[0]
        row += dr
        col += dc
        if 0 <= row < self.height and 0 <= col < self.width:
            self.snake.appendleft((row, col))
            if self.food and self.snake[0] == tuple(self.food[-1]):
                self.food.pop()
            else:
                tmp = self.snake.pop()
                if tmp in self.occupied:
                    self.occupied.remove(tmp)
            if (row, col) in self.occupied:
                return -1
            self.occupied.add((row, col))
            return len(self.snake)-1
        else:
            return -1




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)