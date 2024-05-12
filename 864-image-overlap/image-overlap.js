// declare two variables arr1 and arr2 that will hold on to values from our iteration
// get the dimensions of img1 and img2
// iterate through both images
// if the current cell is a 1, push the dimensions into the respective arrays
// declare a variable lookup that will store the results of the translations
// iterate through arr1 and arr2
// store the diff between dimensions in lookup
// update the maximum overlap so far
// return the overlap at the end of the iterations

var largestOverlap = function(img1, img2) {
    let arr1 = []
    let arr2 = []
    let rows = img1.length
    let columns = img1[0].length
    let lookup = {}
    let overlap = 0

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (img1[i][j] == 1) arr1.push([i, j])
            if (img2[i][j] == 1) arr2.push([i, j])
        }
    }    

    for (let [x, y] of arr1) {
        for (let [i, j] of arr2) {
            translation = [i - x, j - y]
            if (!lookup[translation]) lookup[translation] = 0
            lookup[translation] ++
            overlap = Math.max(overlap, lookup[translation])
        }
    }
    return overlap
};