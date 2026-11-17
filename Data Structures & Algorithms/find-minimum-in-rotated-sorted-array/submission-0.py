class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        res = nums[0]
        while(low<=high):
            if(nums[low]<nums[high]):
                # subarray is already sorted
                res = min(res, nums[low])
                break

            mid = low+(high-low)//2
            res = min(res, nums[mid])
            if(nums[low]<=nums[mid]):
                low=mid+1
            else:
                high = mid-1
                
        return res


