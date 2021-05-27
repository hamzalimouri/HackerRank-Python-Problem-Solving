def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(list(grid[i])))
    for i in range(len(grid[0])):
        temp = grid[0][i]
        for x in grid:
            if x[i] < temp:
                return 'NO'
            temp = x[i]
    return 'YES'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)
