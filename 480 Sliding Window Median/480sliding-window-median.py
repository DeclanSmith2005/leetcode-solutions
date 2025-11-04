from typing import List
from bisect import bisect_left, insort

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])  # sorted window of size k
        res: List[float] = []
        n = len(nums)
        odd = (k % 2 == 1)

        for r in range(k, n + 1):
            # compute median from sorted window
            if odd:
                res.append(float(window[k // 2]))
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            if r == n:   # we've just used the last window
                break

            # element leaving the window: nums[r - k]
            out_num = nums[r - k]
            idx = bisect_left(window, out_num)
            window.pop(idx)

            # element entering the window: nums[r]
            insort(window, nums[r])

        return res
