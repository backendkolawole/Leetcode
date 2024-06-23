// declare a variable output that will be returned
// take the dimension of the matrix
// traverse the matrix in a spiral order while still in bounds

var spiralOrder = function(matrix) {
    let output = []
    let topRow = 0
    let bottomRow = matrix.length - 1
    let leftColumn = 0
    let rightColumn = matrix[0].length - 1

    while (topRow <= bottomRow && leftColumn <= rightColumn) {

        // traverse left to right
        for (let i = leftColumn; i <= rightColumn; i++) {
            output.push(matrix[topRow][i])
        }
        topRow ++


        // traverse top to bottom
        for (let i = topRow; i <= bottomRow; i++) {
            output.push(matrix[i][rightColumn])
        }
        rightColumn --


        if (topRow <= bottomRow) {
            // traverse right to left
            for (let i = rightColumn; i >= leftColumn; i--) {
                output.push(matrix[bottomRow][i])
            }
            bottomRow --

        }

        if (leftColumn <= rightColumn) {
            // traverse bottom to top
            for (let i = bottomRow; i >= topRow; i--) {
                output.push(matrix[i][leftColumn])
            }
            leftColumn++

        }

    }

    return output
        
};