class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = []
        suffixProd = [1 for i in range(len(nums))]
        # print(suffixProd)

        for i in range(len(nums)):
            if i==0:
                prefixProd.append(1)
            elif i==1:
                prefixProd.append(nums[0])
            else:
                prefixProd.append(prefixProd[i-1]*nums[i-1])
        # print(prefixProd)

        n = len(nums)
        for i in range(len(nums)-2,-1,-1):
            suffixProd[i] = suffixProd[i+1]*nums[i+1]
        # print(suffixProd)
        
        ans=[]
        for i in range(len(nums)):
            ans.append(suffixProd[i]*prefixProd[i])
        return ans