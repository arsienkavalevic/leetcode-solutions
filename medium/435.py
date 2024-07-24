# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda i : i[1])

        n = len(intervals)

        prev = 0
        counter = 1

        for i in range(1, n):
            if intervals[prev][1] <= intervals[i][0]:
                counter += 1
                prev = i

        return n - counter