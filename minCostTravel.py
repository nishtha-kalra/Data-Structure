def min_cost_travel(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a 2D dp array to store the minimum cost at each cell
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the starting point
    dp[0][0] = grid[0][0]
    
    # Initialize the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Initialize the first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Fill in the dp array
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    return dp[rows - 1][cols - 1]

# Example grid
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

# Calculate the minimum cost to travel through the grid
min_cost = min_cost_travel(grid)
print(f"The minimum cost to travel through the grid is {min_cost}")
