// traverse the grid row by row
// for each row
// store the row in a lookup table by their frequencies
// take the transpose of the matrix
// count the equal row and column pairs 

var equalPairs = function(grid) {
    let lookup = {}
    count = 0

    for (let row of grid) {
        rowValues = ''
        for (let i = 0; i < row.length; i++) {
            rowValues += row[i] + ' - '
        }
        if (!lookup[rowValues]) lookup[rowValues] = 0
        lookup[rowValues] ++
    }

    function transpose(matrix) {
        let rows = matrix.length
        let columns = matrix[0].length
        let array = Array.from({length: rows}, ()=> new Array(columns))
        
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < columns; j++) {
                array[j][i] = matrix[i][j]
            }
        }

        return array
    }
    
    array = transpose(grid)

    for (let row of array) {
        rowValues = ''
        for (let i = 0; i < row.length; i++) {
            rowValues += row[i] + ' - '
        }
        count += lookup[rowValues] || 0
    }

    console.log(lookup)

    return count
};