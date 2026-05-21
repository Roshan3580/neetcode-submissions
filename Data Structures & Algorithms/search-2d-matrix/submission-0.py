class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        first_row = 0
        last_row = m - 1

        while first_row <= last_row:
            mid_row = (first_row + last_row) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                break
            elif target < matrix[mid_row][0]:
                last_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                first_row = mid_row + 1
            else:
                return false
        
        row = mid_row
        first = 0
        last = n - 1
        while first <= last:
            middle = (first + last) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                first = middle + 1
            elif matrix[row][middle] > target:
                last = middle - 1
            else:
                break
        if first > last:
            return False