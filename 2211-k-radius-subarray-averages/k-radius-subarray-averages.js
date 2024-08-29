// declare a variable avgs which is the result array
// declare a variable window equal to 2 times k plus 1
// get the sum of the elements in the window
// iterate through nums
// if there are less than k elements before or after the current index, then the k-radius average is -1
// else avgs at current index i is the k-radius average for the subarray centered at index i

var getAverages = function(nums, k) {
    let window = (2 * k) + 1
    let sum = 0
    let avgs = new Array(nums.length)

    for (let i = 0; i < window; i++) {
        sum += nums[i]
    }

    for (let i = 0; i < nums.length; i++) {
        if (i < k || i > nums.length - 1 - k) avgs[i] = -1
        else if (i == k) {
            avgs[i] = Math.trunc(sum / window)
        }
        else {
            sum += nums[i + k] - nums[i - k - 1]
            avgs[i] = Math.trunc(sum / window)
        }
    }
    return avgs
};