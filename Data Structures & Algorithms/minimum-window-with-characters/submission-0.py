class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        hashmap1 = {}
        for i in t:
            hashmap1[i] = 1 + hashmap1.get(i, 0)

        need, window = len(hashmap1), [-1,-1]
        length = float('inf')
        l, hashmap2 = 0, {}
        have = 0
        for r in range(len(s)):
            hashmap2[s[r]] = 1 + hashmap2.get(s[r], 0)

            if s[r] in hashmap1 and hashmap1[s[r]] == hashmap2[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < length:
                    window = [l, r]
                    length = r - l + 1

                hashmap2[s[l]] -= 1
                if s[l] in hashmap1 and hashmap2[s[l]] < hashmap1[s[l]]:
                    have -= 1

                l += 1

        l, r = window

        if length != float('inf'):
            return s[l:r+1]
        else:
            return ""

        