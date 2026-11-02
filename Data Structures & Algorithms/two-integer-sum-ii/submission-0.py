class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0 
        j = n-1
        while(j>i):
            res = numbers[i]+numbers[j]
            if(res == target):
                return [i+1,j+1]
            elif (res>target):
                j-=1
            else:
                i+=1
        return [i,j]