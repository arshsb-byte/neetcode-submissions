class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1

        res=0
        while(l<r):
            ans = (r-l)*min(heights[r],heights[l])
            res=max(res,ans)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return res