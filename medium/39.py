# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtrack(current, current_sum, idx):
            if current_sum > target:
                return
            if current_sum == target:
                result.append(current)

            for i in range(idx, n):
                backtrack(current + [candidates[i]], current_sum + candidates[i], i)
            return

        backtrack([], 0, 0)

        return result