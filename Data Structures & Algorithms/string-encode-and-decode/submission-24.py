class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded += f"{length}#{string}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        pointer = 0
        result = []
        while pointer < len(s):
            delimiter = pointer
            while s[delimiter] != '#':
                delimiter += 1
            word = delimiter + 1
            length = int(s[pointer:delimiter])
            result.append(s[word: word + length])
            pointer = word + length
        print(result)
        return result
