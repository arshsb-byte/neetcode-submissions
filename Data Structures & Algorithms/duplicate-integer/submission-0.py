class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hm = {}
        for i in range(len(nums)):
            if nums[i] in Hm:
                return True
            else:
                Hm[nums[i]]=1
        return False
        