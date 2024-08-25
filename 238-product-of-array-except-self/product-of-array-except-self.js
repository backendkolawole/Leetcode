// 
var productExceptSelf = function(nums) {
   let leftMultiply = 1
   let rightMultiply = 1
   let left = []
   let right = []

   for (i = 0; i < nums.length; i++) {
        left[i] = leftMultiply
        leftMultiply *= nums[i]
   }

   for (let i = nums.length - 1; i >= 0; i--) {
    right[i] = rightMultiply * left[i]
    rightMultiply *= nums[i]
   } 

   return right
};