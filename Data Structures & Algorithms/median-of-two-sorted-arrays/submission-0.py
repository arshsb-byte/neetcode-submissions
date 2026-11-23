class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2

        if len(B)<len(A):
            A,B = B,A
        
        a = len(A)
        b = len(B)
        total = a+b
        half = total // 2

        low = 0
        high = a
        while low <= high:
            mid = low + (high - low) // 2
            mid2 = half - mid
            
            a1 = A[mid] if mid < a else float('inf')        # right1
            b1 = B[mid2 - 1] if mid2 > 0 else float('-inf') # left2
            a2 = A[mid - 1] if mid > 0 else float('-inf')   # left1
            b2 = B[mid2] if mid2 < b else float('inf')      # right2

            if a2<=b2 and b1<=a1:
                # median found 
                if(total%2 == 0):
                    return (max(a2, b1) + min(a1, b2)) / 2
                else:
                    return min(a1, b2)
            elif a2 > b2:
                high = mid - 1
            else:
                low = mid + 1