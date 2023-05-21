# https://leetcode.com/problems/contains-duplicate/
# Time: O(n)
# Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()

        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap.add(num)

        return False
