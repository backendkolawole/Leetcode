// declare a function to check if the cell is on a diagonal
// declare three lookup objects to store the count of moves on rows, columns and diagonals
// declare a 3 by 3 array with initial value an empty string
// declare a variable aFirst with initial value equal to true
// iterate through the moves array
// for each move,
// if the index modulo 2 is equal to 0 indicating its As turn,
// if the cell is on the diagonal
// if the diagonal is present in lookup initiate its count to 0
// increment the count of O or X moves in that diagonal
// else increment the count of O or X moves in that row amd column
// if the count of 0 in the row is equal to 3 return B
// else if the count of X in the row or columns is equal to 3 return A
// if the length of the moves is less than 9 return Draw

var tictactoe = function(moves) {
    lookup = {}
 
    grid = Array.from({length: 3}, ()=> new Array(3).fill(''))  


    function isAturn(num) {
        return num % 2 == 0
    }

    function isOnPrimaryDiagonal(i, j) {
        return i - j == 0 
    }

    function isOnSecondaryDiagonal(i, j) {
        return i + j == 2 
    }

    let k = 0
    
    for (let [i, j] of moves) {
        if (isAturn(k)) {
            grid[i][j] = 'X'
            if (isOnPrimaryDiagonal(i, j)) {
                let value = 'X on primary diagonal'
                if (!lookup[value]) lookup[value] = 0
                lookup[value] += 1
                if (lookup[value] == 3) return 'A'
            } 
            if (isOnSecondaryDiagonal(i, j) || i == 1 && j == 1) {
                let value = 'X on secondary diagonal'
                if (!lookup[value]) lookup[value] = 0
                lookup[value] += 1
                if (lookup[value] == 3) return 'A'
            }

            row = `X on row ${i}`
            column = `X on column ${j}`
            if (!lookup[row]) lookup[row] = 0
            lookup[row] += 1
            if (lookup[row] == 3) return 'A'
        
            if (!lookup[column]) lookup[column] = 0
            lookup[column] += 1
            if (lookup[column] == 3) return 'A'
            console.log('it was As turn: ', k, [i, j])
        }
        else {
            grid[i][j] = 'O'
            if (isOnPrimaryDiagonal(i, j)) {
                let value = 'O on primary diagonal'
                if (!lookup[value]) lookup[value] = 0
                lookup[value] += 1
                if (lookup[value] == 3) return 'B'
            } 
            if (isOnSecondaryDiagonal(i, j) || i == 1 && j == 1) {
                let value = 'O on secondary diagonal'
                if (!lookup[value]) lookup[value] = 0
                lookup[value] += 1
                console.log('incrementing O on secondary diagonal: ', k, [i, j])

                if (lookup[value] == 3) return 'B'
            }
            row = `O on row ${i}`
            column = `O on column ${j}`

            if (!lookup[row]) lookup[row] = 0
            lookup[row] += 1
            if (lookup[row] == 3) return 'B'
        
            if (!lookup[column]) lookup[column] = 0
            lookup[column] += 1
            if (lookup[column] == 3) return 'B'
            console.log('it was Bs turn: ', k, [i, j])

        }
        k++
        
    }

    // console.log(k)

    // console.log(lookup)
    // console.log(grid)

    return moves.length == 9? 'Draw': 'Pending'

    
};

