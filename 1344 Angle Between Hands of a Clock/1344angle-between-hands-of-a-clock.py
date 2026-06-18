class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mAng = ((minutes / 60) * 360) % 360
        hAng = (((hour / 12) +((minutes / 60) / 12)) * 360) % 360
        return min(abs(mAng - hAng), 360 - abs((mAng - hAng)))
