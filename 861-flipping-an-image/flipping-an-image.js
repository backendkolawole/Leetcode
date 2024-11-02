
var flipAndInvertImage = function(image) {
    for (let row of image) {
        row.reverse()
    }    
    for (let i = 0; i <= image.length - 1; i++) {
        for (let j = 0; j <= image[0].length - 1; j++) {
            if (image[i][j] == 0) image[i][j] = 1
            else if (image[i][j] == 1) image[i][j] = 0
        }
    }
    return image
};