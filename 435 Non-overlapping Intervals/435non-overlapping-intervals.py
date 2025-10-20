from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end time (second element)
        intervals.sort(key=lambda x: x[1])

        removals = 0
        # keep the end time of the last interval we kept
        last_end = intervals[0][1]

        for s, e in intervals[1:]:
            # if current start < last_end => overlap, we must remove one
            if s < last_end:
                removals += 1
                # we remove the current interval (so last_end stays the same),
                # because keeping the interval with earlier end is optimal
            else:
                # no overlap, keep this interval
                last_end = e

        return removals
