
var isPerfectSquare = function(num) {
    let i = 0
    let j = num

    while (i <=j) {
        let mid = Math.floor((i + j) / 2)
        let squared = mid **2
        if (squared == num) return true
        if (squared > num) j = mid - 1
        else i = mid + 1
    }    
    return false
};