
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Base cases: 1 way for n=1, 2 ways for n=2
        one_step_behind = 2
        two_steps_behind = 1
        
        for _ in range(3, n + 1):
            current = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current
            
        return one_step_behind
