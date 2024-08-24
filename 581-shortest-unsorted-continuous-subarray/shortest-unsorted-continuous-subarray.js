
var findUnsortedSubarray = function(nums) {
    let sorted = [...nums].sort((a, b) => a - b)
    let size = nums.length
    let left = size
    let right = 0

    for (let i = 0; i < size; i++) {
        if (nums[i] != sorted[i]) {
            left = Math.min(i, left)
            right = Math.max(i, right)
        }
    }

    if (left == size) return 0

    return right - left + 1
};

// var findUnsortedSubarray = function(nums) {
//     let n = nums.length;
//     let sortedNums = [...nums].sort((a, b) => a - b);
//     let left = 0, right = n - 1;

//     while (left < n && nums[left] === sortedNums[left]) {
//         left++;
//     }

//     if (left === n) {
//         return 0; // the array is already sorted
//     }

//     while (right >= 0 && nums[right] === sortedNums[right]) {
//         right--;
//     }

//     return right - left + 1;
// };