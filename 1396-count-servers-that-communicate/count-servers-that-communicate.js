// take the dimensions of the grid
// declare a variable lookup that will store servers in rows and columns
// iterate through the grid
// for each server 
// if there is a server present on that cell or on that row in the lookup object increment the server count by 1
// else add the cell to the row and column in the lookup  object

var countServers = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    let rowCount = {}
    let columnCount = {}
    let serverCount = 0

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]
            if (cell == 1) {
                if (!rowCount[i]) rowCount[i] = 0
                rowCount[i] ++
                if (!columnCount[j]) columnCount[j] = 0
                columnCount[j] ++
            }
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            cell = grid[i][j]
            if (cell == 1) {
                if (rowCount[i] > 1 || columnCount[j] > 1) serverCount ++
            }
        }
    }

    return serverCount
};