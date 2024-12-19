// iterate through 
var diagonalSort = function(mat) {
    let lookup = {}
    let rows = mat.length 
    let columns = mat[0].length

    for (i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            const diagonal = i - j
            const cell = mat[i][j]
            if (!lookup[diagonal]) {
                lookup[diagonal] = []
            }
            lookup[diagonal].push(cell)
        }
    }

    for (let key in lookup) {
        lookup[key].sort((a, b)=> a - b)
    }

    for (i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            diagonal = i - j
            mat[i][j] = lookup[diagonal].shift()
        }
    } 
    return mat
};