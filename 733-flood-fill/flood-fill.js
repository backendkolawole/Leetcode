var floodFill = function(image, sr, sc, color) {
    if (image[sr][sc] == color) {
        return image
    }
    let rows = image.length
    let columns = image[0].length

    function traverse(i, j, start_color) {
        if (i < 0 || j < 0 || i == rows || j == columns || image[i][j] != start_color) return
        image[i][j] = color
        traverse(i - 1, j, start_color)
        traverse(i, j + 1, start_color)
        traverse(i + 1, j, start_color)
        traverse(i, j - 1, start_color)
    }

    traverse(sr, sc, image[sr][sc])
    return image
};