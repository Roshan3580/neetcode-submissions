class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                mid_row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        if l > r:
            return False
        
        l, r = 0,  len(matrix[mid_row]) - 1
        while l <= r:
            mid = l + (r - l)//2
            if matrix[mid_row][mid] == target:
                return True
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False