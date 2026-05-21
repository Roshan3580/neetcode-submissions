class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum())
        string = string.lower()
        print(string)
        print(string[::-1])
        if string == string[::-1]:
            return True
        else:
            return False