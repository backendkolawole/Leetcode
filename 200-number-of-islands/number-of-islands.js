// run dfs on the grid
// count the number of islands

var numIslands = function(grid) {
    let rows = grid.length
    let columns = grid[0].length
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    count = 0

    function isValid(i, j) {
        if (i < 0 || i == rows || j < 0 || j == columns || grid[i][j] != "1") return false
        grid[i][j] = "0"
        return true
    }

    function traverse(i, j) {
        for (let direction of directions) {
            let [x, y] = direction
            if (isValid(i + x, y + j)) traverse(i + x, y + j)
        }
    }   

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (grid[i][j] == "1") {
                count +=1
                traverse(i, j)
            }
        }
    }

    return count






};