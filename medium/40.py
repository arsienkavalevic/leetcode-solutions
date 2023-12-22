# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def backtrack(current, current_sum, index):
            if current_sum > target:
                return
            if current_sum == target:
                result.append(current)

            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(current + [candidates[i]], current_sum + candidates[i], i + 1)
            return

        backtrack([], 0, 0)
        
        return result