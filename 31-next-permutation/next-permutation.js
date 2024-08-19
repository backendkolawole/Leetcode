// get break point index
// iterate through the array from right to left
// if the num at current index is greater than the number at index plus 1

// if the index is - 1
// reverse nums and return it

// [2 1 5 4 3 0 0]
// else find the first elem greater than the elem at the break point index
// swap the elem at the break point index and the first greater elem

// reverse the remaining sorted elements

var nextPermutation = function(nums) {
    let length = nums.length
    let index = nums.length -2

    while (index >= 0 && nums[index] >= nums[index + 1]) {
        index -= 1
    }
    if (index == -1) return nums.reverse()

    let swap = length - 1

    while (nums[swap] <= nums[index]) swap --
    [nums[swap], nums[index]] = [nums[index], nums[swap]]

    let i = index + 1
    let j = length - 1

    while (i < j) {
        [nums[i], nums[j]] = [nums[j], nums[i]]
        i++
        j--
    }
};