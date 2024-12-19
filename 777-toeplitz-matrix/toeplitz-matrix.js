var isToeplitzMatrix = function(matrix) {
    let rows = matrix.length
    let columns = matrix[0].length

    function isDiagonalUnivalue(i, j) {
        let start_value = matrix[i][j]

        while (i < rows && j < columns) {
            if (matrix[i][j] != start_value) return false
            i +=1
            j += 1
        }
        return true
    } 

    for (let i = 0; i < columns; i++) {
        if (!isDiagonalUnivalue(0, i)) {
            return false
        }
    }    

    for (let i = 1; i < rows; i++) {
        if (!isDiagonalUnivalue(i, 0)) {
            return false
        }
    }
    return true
};