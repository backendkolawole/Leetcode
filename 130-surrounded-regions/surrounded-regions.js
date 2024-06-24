var solve = function(board) {
    let rows = board.length
    let columns = board[0].length

    function capture(r, c) {
        if ((r < 0 || c < 0) || (r == rows || c == columns) || board[r][c] != "O") return
        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)
    }

    // iterate through the board row by row
    // capture unsurrounded regions
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if ((board[i][j] == "O") && ((i == 0 || i == rows - 1) || (j == 0 || j == columns - 1))) capture(i, j)
        }
    }

    // iterate through the board row by row
    // capture surrounded regions

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (board[i][j] == "O") board[i][j] = "X"
            else if (board[i][j] == "T") board[i][j] = "O"
        }
    }

    // iterate through the board row by row
    // uncapture surrounded regions
    // for (let i = 0; i < rows; i++) {
    //     for (let j = 0; j < columns; j++) {
    //     }
    // }    
};