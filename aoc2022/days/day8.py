from math import prod


def sum_grid(grid: list):
    """
    Look at each cell in the grid row by row, then column by column for each row.
    For each cell (row[col]), create a list of all the other cells in each direction
    that are greater than or equal to the current cell. The length of this list is the number
    of trees blocking the view from that direction. So if the length of the list for a
    given direction is zero, then the current cell is visible from that direction.

    - Left: check/append every previous item in the current row
    - Right: check/append every item from the current cell, up to the last item in the row list
    - Up: check/append the cell in the current column from all previous rows
    - Down: check/append the cell in the current column from all rows after the current row
    """

    for r in range(1, len(grid)-1):
        for c in range(1, len(grid)-1):
            tracker = {
                'left':     len([x for x in grid[r][:c] if x >= grid[r][c]]),
                'right':    len([x for x in grid[r][c + 1:] if x >= grid[r][c]]),
                'up':       len([y[c] for y in grid[:r] if y[c] >= grid[r][c]]),
                'down':     len([y[c] for y in grid[r + 1:] if y[c] >= grid[r][c]]),
            }
            if any([d == 0 for d in tracker.values()]):
                yield 1


def prod_scenic_score(grid: list):
    """
    Look at each cell in the grid row by row, then column by column for each row.
    For each cell (row[col]), create a list of all the cells in each of the four directions.
    Then for each cell in each of these directions, compare that cell to the current cell.
    If that cell is greater than or equal to the current cell, then we've reached the last
    visible tree. Multiply the number of trees visible from the current cell, and save this
    product in a list. Return the largest of these products.
    """

    best_scenic_score = 0

    for r in range(1, len(grid)-1):
        for c in range(1, len(grid)-1):
            scenery = []
            scenery_directions = [
                list(reversed([x for x in grid[r][:c]])),           # All cells to the left
                [x for x in grid[r][c + 1:]],                       # All cells to the right
                list(reversed([y[c] for y in grid[:r] if y[c]])),   # All cells above
                [y[c] for y in grid[r + 1:] if y[c]],               # All cells below
            ]
            
            for direction in scenery_directions:
                for d in range(len(direction)):
                    if direction[d] >= grid[r][c]:
                        break
                scenery.append(d+1)

            scenic_score = prod(scenery)
            best_scenic_score = max(best_scenic_score, scenic_score)

    return best_scenic_score


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [line.strip() for line in f]
        grid = [list(map(int, [*line])) for line in content]
        
        """
        grid = [[3,0,3,7,3],
                [2,5,5,1,2],
                [6,5,3,3,2],
                [3,3,5,4,9],
                [3,5,3,9,0]]
        """

        grid_shape = (len(grid), len(grid[0]))
        grid_border_count = (grid_shape[0] * 2) + (grid_shape[1] * 2) - 4
        grid_total_sum = sum(sum_grid(grid)) + grid_border_count
        grid_scenic_score = prod_scenic_score(grid)

        print(f'[+] Part 1 solution: {grid_total_sum}')
        print(f'[+] Part 2 solution: {grid_scenic_score}')

