class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = sorted(Counter(word).values(), reverse=True)

        ans = 0
        for i, freq in enumerate(freqs):
            ans += freq * (i // 8 + 1)

        return ans