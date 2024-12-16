// use a lookup object to find if the current cell is present in any row, column or subbox

isValidSudoku = function(board) {
    let rows = board.length 
    let columns = board[0].length
    let lookup = {}

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = board[i][j]
            let subBoxIndex = (3 * Math.floor(i / 3)) + Math.floor(j / 3)

            if (cell != '.') {
                let row = `row: ${i}, cell: ${cell}`
                let column = `column: ${j}, cell: ${cell}`
                let subBox = `subBox: ${subBoxIndex}, cell: ${cell}`
                if (row in lookup || column in lookup || subBox in lookup) return false
                lookup[row] = true
                lookup[column] = true
                lookup[subBox] = true
            }
        }
    }
    return true
};