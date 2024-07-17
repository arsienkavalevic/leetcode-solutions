# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        land_p = set()
        land_a = set()

        r, c = len(heights), len(heights[0])

        def dfs(i, j, land):
            land.add((i, j))
            dirs = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))
            for x, y in dirs:
                if (
                    0 <= x < r
                    and 0 <= y < c
                    and heights[x][y] >= heights[i][j]
                    and (x, y) not in land
                ):
                    dfs(x, y, land)
        
        for i in range(r):
            dfs(i, 0, land_p)
            dfs(i, c - 1, land_a)
        for j in range(c):
            dfs(0, j, land_p)
            dfs(r - 1, j, land_a)

        return list(land_p & land_a)