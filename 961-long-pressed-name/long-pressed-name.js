
var isLongPressedName = function(name, typed) {
    // if (name.length == typed.length) return true
    if (name.length > typed.length) return false

    let i = 0
    let j = 0

    while (j < typed.length) {
        if (name[i] == typed[j]) {
            i ++
        }
        else if (j == 0 || typed[j] != typed[j - 1]) return false
        j++
    }    
    return i == name.length
};