class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [[] for i in range(len(position))]
        times = []
        for i in range(len(position)):
            stack[i] = (position[i], speed[i])
        stack.sort(reverse=True)

        print(stack)

        for p, s in stack:
            time = (target - p)/s     
            times.append(time)
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()
        return len(times)