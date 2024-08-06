# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# traverse the tree
# use bfs
# current sum - node.val is equal to the previous sum
# if the previous sum is present in lookup
# increment the count by the freq of the previous sum in lookup


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        lookup = {0: 1}
        count = 0

        def traverse(node, current_sum):
            nonlocal lookup
            nonlocal count
            if (not node):
                return
            
            current_sum += node.val 
            difference = current_sum - targetSum
            print(current_sum, difference)
            if (difference in lookup):
                print(f"found difference in lookup {difference}")
                count += lookup[difference]
            if (current_sum not in lookup):
                lookup[current_sum] = 1
            else:
                lookup[current_sum] += 1
                
            traverse(node.left, current_sum)
            traverse(node.right, current_sum)
            lookup[current_sum] -= 1

        traverse(root, 0)
        return count


        