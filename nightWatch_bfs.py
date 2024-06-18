'''
You are on a night watch in a mall, represented as an n x m grid:

'x' denotes areas blocked by walls, fountains, etc., and are not traversable.
'o' denotes open spaces that the security guard can explore.
Your task is to find the shortest distances from a given starting position to every other reachable point in the grid.

eg.

[['o', 'o', 'x', 'o'],
 ['x', 'o', 'o', 'o'],
 ['o', 'o', 'x', 'o']]

 Starting Poing  = [0, 1]

 Output

 [[1, 0, -1, 4],
 [-1, 1, 2, 3],
 [3, 2, -1, 4]]
 '''

def shortest_distances(grid, start):
    n = len(grid)
    m = len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = [start]
    distances = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(-1)
        distances.append(row)
    distances[start[0]][start[1]] = 0
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'o' and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    print(distances)
grid = [['o', 'o', 'x', 'o'],
 ['x', 'o', 'o', 'o'],
 ['o', 'o', 'x', 'o']]
start = [0, 1]
shortest_distances(grid, start)

    
    
    
