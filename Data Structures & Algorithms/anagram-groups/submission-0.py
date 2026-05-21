class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        new_list = []
        for word in strs:
            words = list(word)
            words.sort()
            new_word = ''.join(words)
            if new_word in hashmap:
                hashmap[new_word].append(word)
            else:
                hashmap[new_word] = [word]
        for key in hashmap:
            new_list.append(hashmap[key])
        return new_list
        