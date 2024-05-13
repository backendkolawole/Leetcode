// declare a result variable with same dimensions as the grid
// declare a variable temp that is an empty array at first
// iterate through the grid and store all elements of the grid in temp
// rotate temp
// iterate through result and fill with elements of temp

var shiftGrid = function(grid, k) {

    function rotate(arr, i, j) {

        while (i < j) {
            [arr[i], arr[j]] = [arr[j], arr[i]]
            i += 1
            j -= 1
        }
    
    }

    let temp = []
    let rows = grid.length
    let columns = grid[0].length
    let size = rows * columns
    k %= size

    for (let i = 0; i < rows; i ++) {
        for (let j = 0; j < columns; j++) {
            temp.push(grid[i][j])
        }
    }
    

    let i = 0
    let j = temp.length - 1
    rotate(temp, i, j)
    rotate(temp, i, k - 1)
    rotate(temp, k, j)
    console.log(temp)

    let a = 0

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            grid[i][j] = temp[a]
            a++
        }
    }

    return grid
};