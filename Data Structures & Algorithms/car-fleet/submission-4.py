class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = []
        car = []
        for i in range(len(position)):
            car.append((position[i],speed[i]))
        car.sort()
        car.reverse()
        time = []
        for p, s in car:
            expected_time = (target - p)/s
            time.append(expected_time)
        print(time)
        for i in range(len(time)):
            if i == 0:
                result.append(time[i])
            else:
                if time[i] <= result[-1]:
                    continue
                else:
                    result.append(time[i])
        
        return len(result)
