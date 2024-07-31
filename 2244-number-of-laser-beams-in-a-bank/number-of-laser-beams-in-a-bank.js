var numberOfBeams = function(bank) {
    let prev = 0
    let result = 0

    for (let floor of bank) {
        let curr = 0
        for (let i = 0; i < floor.length; i++) {
            if (floor[i] == "1") curr ++
        }
        if (curr) {
            result += prev * curr
            prev = curr
        }
    }   
    return result
};