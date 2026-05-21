class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        res = 0
        mostfreq = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            mostfreq = max(mostfreq, freq[s[r]])

            while k < (r - l + 1) - mostfreq:
                freq[s[l]] = freq.get(s[l]) - 1
                l += 1

            res = max(res, r-l+1)
        return res