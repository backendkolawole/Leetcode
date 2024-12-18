var imageSmoother = function(img) {

    let rows = img.length
    let columns = img[0].length
    let temp = Array.from({length: rows}, () => new Array(columns))
    let positions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

    function checkNeighbor(i, j) {
        if (i < 0 || j < 0 || i == rows || j == columns) return [0, 0]
        else {
            return [img[i][j], 1]
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            let sum = 0
            let num = 0
            let average = 0

            for (let [x, y] of positions) {
                [a, b] = checkNeighbor(i + x, j + y) 
                sum += a
                num += b
            }
            average = Math.floor((sum + img[i][j]) / (num + 1))
            temp[i][j] = average

        }
    }

    return temp



};