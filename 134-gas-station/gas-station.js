
var canCompleteCircuit = function(gas, cost) {
    let start = gas.length - 1
    let next = 0
    let gasInTank = gas[start] - cost[start]

    while (start >= next) {
        if (gasInTank >= 0 ){
            gasInTank += gas[next] - cost[next] 
            next += 1
        }
        else {
            start --
            gasInTank += gas[start] - cost[start]
        }
    }
    return gasInTank >= 0 ? start : -1
};