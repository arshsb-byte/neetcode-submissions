class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        timeLeft = [[0 for x in range(2)] for x in range(n)]
        for i in range(n):
            timeLeft[i][0] = position[i]
            timeLeft[i][1] = (target-position[i])/speed[i]
        
        timeLeft.sort(key=lambda a: a[0] , reverse=True)

        fleetCount = 0
        prevTime = 0

        for car in timeLeft:
            if(car[1]>prevTime):
                fleetCount+=1
                prevTime = car[1]

        return fleetCount
        