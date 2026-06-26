class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        count = {}

        for c in t:
            target[c] = target.get(c, 0) + 1

        res, resLen = float('inf'), [-1, -1]
        l = 0
        have, need = 0, len(target)

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if s[r] in target and count[s[r]] == target[s[r]]:
                have +=1
            while have == need:
                if r - l + 1 < res:
                    resLen = [l, r]
                    res = r - l + 1
                count[s[l]] -= 1
                if s[l] in target and target[s[l]] > count[s[l]]:
                    have -= 1
                l += 1
        left, right = resLen
        if res != float('inf'):
            return s[left:right+1]
        else:
            return ""
                