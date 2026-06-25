class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        mfreq = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            mfreq = max(mfreq, count[s[r]])

            while (r - l + 1) - mfreq > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            res = max(res, r - l + 1)
        return res

