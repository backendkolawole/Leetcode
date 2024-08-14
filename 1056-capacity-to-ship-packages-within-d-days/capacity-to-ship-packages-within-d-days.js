// use bs
// declare two boundary variables i and j with initial values the max weight and the sum of all weights
// check the mid weight as current weight
// if the we canship all the packages at current day, reduce weight
// else increase the weight

// define a function canShip that takes in a current weight
// declare a variable no_days with initial value 0
// declare a variable weight with initial value 0
// iterate through weights
// increment the no of days
// add the current weight to load
// if the load goes above current weight, reset current weight to 0 

var shipWithinDays = function(weights, days) {

    function canShip(weight) {
        let noOfDays = 1
        let totalWeight = 0

        for (let w of weights) {
            totalWeight += w
            if (totalWeight > weight) {
                noOfDays ++
                totalWeight = w
            }
        }
        return noOfDays <= days
    }

    let i = Math.max(...weights)
    let j = weights.reduce((a, b) => a + b, 0)

    while (i <= j) {
        let weight = Math.floor((i + j) / 2)

        if (canShip(weight)) j = weight - 1
        else i = weight + 1
    }
    return i
};