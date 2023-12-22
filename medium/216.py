# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for comb in combinations(range(1, 10), k):
            if sum(comb) == n:
                result.append(comb)
        return result