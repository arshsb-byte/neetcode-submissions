class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        maxL = height[l]
        maxR = height[r]

        total=0

        while(l<r):
            if(maxL>maxR):
                r-=1
                maxR = max(maxR,height[r])
                total+=maxR-height[r]
            else:
                l+=1
                maxL = max(maxL,height[l])
                total+=maxL-height[l]
        return total


        #O(n) memory
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        if(n<=2):
            return 0

        for i in range(1,n-1,1):
            leftMax[i] = max(leftMax[i],leftMax[i-1],height[i-1])
        
        # print(leftMax)

        for i in range(n-2,0,-1):
            rightMax[i] = max(rightMax[i],rightMax[i+1],height[i+1])

        ans = 0
        for i,a in enumerate(height):
            ans+=max(min(leftMax[i],rightMax[i]) - a,0)
        
        return ans