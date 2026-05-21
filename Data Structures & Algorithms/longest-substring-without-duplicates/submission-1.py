class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        left = 0
        count = 0
        for i in range(len(s)):
            while s[i] in hashmap:
                hashmap.remove(s[left])
                left += 1
            hashmap.add(s[i])
            count = max(count, i - left + 1)
        return count