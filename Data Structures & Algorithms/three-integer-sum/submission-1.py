class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n = len(nums)
        nums.sort()
        
        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == a:
                continue
            else:
                l,r = i+1,n-1
                while(l<r):
                    Tsum = nums[l]+nums[r]+a
                    if(Tsum>0):
                        r-=1
                    elif(Tsum<0):
                        l+=1
                    else:
                        res.append([a,nums[l],nums[r]])
                        l+=1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
        return res



        