
var dailyTemperatures = function(temperatures) {
    let stack = []
    let ans = new Array(temperatures.length).fill(0)

    for (let i = temperatures.length -1; i >= 0; i--) {
        temp = temperatures[i]

        if (!stack.length) {
            stack.push([temp, i])
            continue
        }
        while (stack.length && temp >= stack.at(-1)[0]) {
            stack.pop()
        }
        if (stack.length) {
            ans[i] = stack.at(-1)[1] - i
            stack.push([temp, i])
        } else {
            stack.push([temp, i])
        }
    }    
    return ans
};