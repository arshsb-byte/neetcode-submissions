class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1
        high = max(piles)
        nearestK = 1

        while low<=high:
            mid = low + (high-low)//2
            totalTime = 0
            for x in piles:
                totalTime += math.ceil(x/mid)
            if(totalTime > h):
                low = mid+1
            elif(totalTime <= h):
                high = mid-1
                nearestK = mid
        return nearestK


        