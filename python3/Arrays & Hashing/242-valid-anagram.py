# https://leetcode.com/problems/valid-anagram/
# Time: O(n)
# Space: O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the strings are different, which means they can't be anagrams
        if len(s) != len(t):
            return False

        # Initialize two empty dictionaries to count the occurrences of characters in both strings
        counterS = {}
        counterT = {}

        # Iterate through each character in the strings
        for i in range(len(s)):
            # Increment the count of the character in the respective dictionary
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)

        # Check if the two dictionaries are equal, which means the strings are anagrams
        return counterS == counterT
