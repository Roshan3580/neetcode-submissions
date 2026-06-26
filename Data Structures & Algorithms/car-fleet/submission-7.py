class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [[position[i], speed[i]] for i in range(len(position))]
        
        cars.sort(reverse=True)
        for p, s in cars:
            time = (target - p)/s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
            
        return len(stack)