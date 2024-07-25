
var orangesRotting = function(grid) {
    let queue = []
    let steps = 0
    let freshOranges = 0
    let rows = grid.length
    let columns = grid[0].length

    function isValid(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns || grid[i][j] != 1) return false
        return true
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (grid[i][j] == 1) {
                freshOranges += 1
            }
            if (grid[i][j] == 2) {
                queue.push([i, j])
            }
        }
    }

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


    while (queue.length && freshOranges > 0) {
        size = queue.length

        for (let i = 0; i < size; i++) {
            [x, y] = queue.shift()

            for (let [dr, dc] of directions ){
                newX = dr + x
                newY = dc + y

                if (isValid(newX, newY)) {
                    grid[newX][newY] = 2
                    queue.push([newX, newY])
                    freshOranges -= 1
                }

            }

        }
        steps += 1


    }

    return freshOranges == 0? steps: -1


};