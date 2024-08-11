var myAtoi = function(s) {
    s = s.trim()
    if (!s) return 0

    i = 0
    let sign = 1

    let char = s[i]
    if (char == '+') {
        i += 1
    }
    
    else if (char == '-') {
        sign = -1
        i += 1
    }

    let result = ""
    while (i < s.length) {
        let cur = s[i]

        if (isNaN(cur) || cur == ' ') {
            break
        }

        else result += cur 
        
        i ++
    
    }

    if (result) {
        result = parseInt(result) * sign
        if (result <= (Math.pow(-2, 31))) return (Math.pow(-2, 31));
        else if (result >= (Math.pow(2, 31) - 1)) return (Math.pow(2, 31) - 1);
        else return result;
    }
    return 0;


};