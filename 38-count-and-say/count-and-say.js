// declare a pointer variable i with initial value equal to 0
// declare a variable result with initial value 1
// while n is greater than or equal to 0
// declare a variable count that will count the number of same characters in the sequence
// while in bounds and the next char in result is equal to the curent char
// increment count 
// build string
// reset count
// decrement n

var countAndSay = function(n) {
    let i = 0
    let result = "1"
    if (n <= 0) return ""
    if (n == 1) return "1"

    while (n > 1) {

        let string = ""
        let count = 1
        let cur = result[0]

        for (let i = 1; i < result.length + 1; i++) {
            console.log(result[i])
            if (result[i] != cur) {
                string += `${count}${cur}`
                cur = result[i]
                count = 1
            }
            else {
                count++
            }

        }
        result = string
        // console.log(string)
        // while (cur == result[i + 1]) {
        //     console.log(cur, result[i + 1])
        // }
        // string += count + cur
        // console.log(string)

        // count = 0


        // result = string

        n --
    }   
    return result
};