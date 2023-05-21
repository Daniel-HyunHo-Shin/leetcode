# https://leetcode.com/problems/two-sum/description/
# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        # Iterate through the range of indices of the array
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]

            num_dict[num] = i

        return []
