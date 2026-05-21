class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            new_word = ''.join(sorted(word))
            if new_word in result:
                result[new_word].append(word)
            else:
                result[new_word] = [word]
        return list(result.values())