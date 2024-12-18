// iterate through the grid
// if the current cell is land, increase the perimeter by 4
// if the current cell has a left neighbor, decrease the perimeter by 2
// if the current cell has a right neightbor, decrease perimeter by 2
// return perimeter

var islandPerimeter = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let perimeter = 0

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]
            if (cell == 1) {
                perimeter += 4
                if (j - 1 >= 0 && grid[i][j - 1] == 1) perimeter -= 2
                if (i - 1 >= 0 && grid[i - 1][j] == 1) perimeter -= 2
            }
        }
    }

    return perimeter
    
};