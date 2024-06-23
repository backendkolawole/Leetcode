// take the transpose of the matrix
// rotate the rows in the matrix

var rotate = function(matrix) {

    let size = matrix.length

    for (let i = 0; i < size; i++) {
        for (let j = i; j < size; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        }
    }

    for (let row of matrix) {
        row.reverse()
    }
    
    
};
