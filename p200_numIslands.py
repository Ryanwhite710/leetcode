"""
200. Number of Islands
Medium
Topics
premium lock icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

"""
# 🔍 Step 1: What is the function supposed to return?

## ✅ Question:
What are we trying to count in this grid?

## ✅ Answer:
We need to return the number of **islands** in the 2D grid.

---

## 🔁 Follow-Up Clarifying Questions:

- What is an island in this context?
- How do I know when a new island starts?
- How are cells connected? 
  - Horizontally? Vertically? Diagonally?
- What are the values in the grid?
  - What does `'1'` represent?
  - What does `'0'` represent?

---

## 🚧 What we learn from the prompt:

- `'1'` = **land**
- `'0'` = **water**
- An island is a **group of '1's connected horizontally or vertically** (not diagonally)

---

## 🧠 Summary:
- You are given a `List[List[str]]` 2D grid.
- Each **contiguous group of '1's** is considered one island.
- You must count how many **separate islands** exist.
"""


from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # Check bounds
                    if (
                        0 <= new_row < rows and
                        0 <= new_col < columns and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visit
                    ):
                        queue.append((new_row, new_col))
                        visit.add((new_row, new_col))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
output = sol.numIslands(grid)
print(output)