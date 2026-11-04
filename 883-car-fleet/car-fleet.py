class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair, reverse=True):
            time = (target - p) / float(s)
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)