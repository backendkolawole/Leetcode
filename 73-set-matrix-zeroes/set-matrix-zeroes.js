// declare two variables with initial values set to false
// iterate through the matrix
// if the current cell is a zero
// if the current cell is in the first row or first column, set the first row or first column variables equal to true
// else set the outermost row or column cell equal to zero

var setZeroes = function(matrix) {
    let firstRow = false
    let firstColumn = false
    let rows = matrix.length
    let columns = matrix[0].length

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let cell = matrix[i][j]
            if (cell == 0) {
                if (i == 0) firstRow = true
                if (j == 0) firstColumn = true
                else {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }
    }

    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < columns; j++) {
            if (matrix[i][0] == 0) matrix[i][j] = 0
            else if (matrix[0][j] == 0) matrix[i][j] = 0
        }
    }

    if (firstRow) {
        for (let i = 0; i < columns; i++) {
            matrix[0][i] = 0
        }
    }

    if (firstColumn) {
        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0
        }
    }
};