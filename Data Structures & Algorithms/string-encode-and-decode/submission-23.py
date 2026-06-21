class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded += f"{length}:{string}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        
        while pointer < len(s):
            delimiter = pointer

            while s[delimiter] != ':':
                delimiter += 1
            length = int(s[pointer:delimiter])
            res.append(s[delimiter + 1: delimiter+length + 1])
            pointer = delimiter + length + 1
        return res

