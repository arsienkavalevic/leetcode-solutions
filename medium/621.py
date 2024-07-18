# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort(reverse=True)

        amount = freq[0] - 1
        idle = n * amount

        for i in range(1, 26):
            idle -= min(amount, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)