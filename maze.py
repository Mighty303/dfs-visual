def dfs_solve_maze_recursive(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    def dfs(r, c):
        # Base cases
        # (1) We reached the end
        # (2) Out of bounds or wall or already visited
        if (r, c) == end:
            path.append((r, c))
            return True
        if (r, c) in visited or maze[r][c] == 1:
            return False
        visited.add((r, c))
        path.append((r, c))
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            # Check bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                # Recursively visit neighbors
                if dfs(nr, nc):
                    return True
        # Backtrack
        path.pop()
        return False

    if dfs(start[0], start[1]):
        return path
    return None

# Example usage:
if __name__ == "__main__":
    maze = [
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1]
    ]
    start = (0, 1)
    end = (5, 6)
    path = dfs_solve_maze_recursive(maze, start, end)