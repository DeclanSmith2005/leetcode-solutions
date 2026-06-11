class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        while asteroids and mass >= asteroids[-1]:
            mass += asteroids.pop()
        return len(asteroids) == 0