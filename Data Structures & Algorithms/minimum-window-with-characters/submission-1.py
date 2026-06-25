class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count, target = {}, {}
        for c in t:
            target[c] = target.get(c, 0) + 1

        have, need = 0, len(target)
        res, resLen = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if s[r] in target and count[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l, r]

                count[s[l]] -= 1
                if s[l] in target and target[s[l]] > count[s[l]]:
                    have -= 1
                l += 1
        if res == [-1, -1]:
            return ""
        else:
            l, r = res
            return s[l:r+1]

            