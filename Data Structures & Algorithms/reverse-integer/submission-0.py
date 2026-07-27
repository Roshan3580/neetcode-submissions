class Solution:
    def reverse(self, x: int) -> int:
        save = x
        x = abs(x)
        number = int(str(x)[::-1])
        
        if save < 0:
            number *= -1
        
        if number < (-1 << 31) or number > (1 << 31) - 1:
            return 0
        return number