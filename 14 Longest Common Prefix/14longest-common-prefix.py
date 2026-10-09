class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        root = strs[0]
        for i, l in enumerate(root):
            for word in strs:
                if i == len(word) or word[i] != l:
                    return root[:i]
        return root