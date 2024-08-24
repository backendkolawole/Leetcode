// declare a variable size equal to the max length of version1 and version2
// declare two pointer variables i and j with initial values 0
// itereate through the two version numbers while the two pointers are still in bounds
// if the string at the two pointers are equal move both pointers 1
// if the char at either pointer is a 0, move the pointer forward
// else if version 1 is less than version2 return - 1
// else if return 1
// return 0 outside the while looop

var compareVersion = function(version1, version2) {
    let size = Math.max(version1.length, version2.length)
    let array1 = (version1.split('.'))
    let array2 = (version2.split('.'))

    let revision1 = ""
    let revision2 = ""

    for (let i = 0; i < Math.max(array1.length, array2.length); i++) {
        revision1 = parseInt(array1[i]) || 0
        revision2 = parseInt(array2[i]) || 0
        if (revision1 < revision2) return -1
        if (revision1 > revision2) return 1
    }


    return 0
};