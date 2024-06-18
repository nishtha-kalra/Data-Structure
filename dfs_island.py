'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
def dfs(arr, row, col):
    n = len(arr)
    m = len(arr[0])
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if 0 <= r < n and 0 <= c < m and arr[r][c] == '1':
            # mark it as visited
            arr[r][c] = '0'
            stack.append((r+1, c))
            stack.append((r-1, c))
            stack.append((r, c+1))
            stack.append((r, c-1))
            
    
def numIslands(grid):
    if not grid:
        return 0
    n = len(grid)
    m = len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)
    return (count)
# Example usage
grid1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
ans1 = numIslands(grid1)
print(ans1) # Output: 1

grid2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
ans2 = numIslands(grid2)
print(ans2) # Output: 3
