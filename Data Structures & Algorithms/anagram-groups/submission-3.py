class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char)-ord('a')] += 1
            hashmap[tuple(count)].append(string)

        for key, value in hashmap.items():
            result.append(value)
        return result