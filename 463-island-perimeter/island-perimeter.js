// iterate the grid row by row
// if we are on land
// if theres a neighbor to the left, reduce the perimeter by 2
// if theres a neigbor at the top, reduce the perimeter by 2

var islandPerimeter = function(grid) {
    let perimeter = 0
    let rows = grid.length
    let columns = grid[0].length

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]

            if (cell == 1) {
                perimeter += 4
                if (j > 0 && grid[i][j - 1] == 1) perimeter -= 2
                if (i > 0 && grid[i - 1][j] == 1) perimeter -= 2
            }
        }
    }

    return perimeter    
};