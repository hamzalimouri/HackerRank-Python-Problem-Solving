def cavityMap(grid):
    n = len(grid[0])
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] > max(grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]):
                grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]
    return grid


if __name__ == '__main__':
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))
