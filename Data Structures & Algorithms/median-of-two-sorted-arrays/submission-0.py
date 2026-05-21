class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = (len(nums1) + len(nums2))
        window = total//2
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums2) - 1
        while True:
            i = (l + r) // 2
            j = window - i - 2

            num2left = nums2[i] if i >= 0 else float("-infinity")
            num2right = nums2[i+1] if i+1 < len(nums2) else float("infinity")
            num1left = nums1[j] if j >= 0 else float("-infinity")
            num1right = nums1[j+1] if j+1 < len(nums1) else float("infinity")

            if num2left <= num1right and num1left <= num2right:
                if total % 2 == 0:
                    return (max(num1left, num2left) + min(num2right, num1right))/2
                else:
                    return min(num2right, num1right)
            elif num1right < num2left:
                r = i - 1
            elif num2right < num1left:
                l = i + 1
            
