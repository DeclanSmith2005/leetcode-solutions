class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = [0] * 26

        for char in s:
            counts[ord(char) - ord('a')] += 1

        left = []
        middle = ""

        for i, count in enumerate(counts):
            char = chr(ord('a') + i)

            # Half of every character goes on the left.
            left.extend([char] * (count // 2))

            # A palindrome can have at most one odd-frequency character.
            if count % 2 == 1:
                middle = char

        left = "".join(left)
        return left + middle + left[::-1]