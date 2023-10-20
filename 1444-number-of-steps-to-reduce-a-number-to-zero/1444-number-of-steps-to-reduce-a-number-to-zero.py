class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num % 2 == 0:
            count = 1 + self.numberOfSteps(num/2)
        else:
            count = 1 + self.numberOfSteps(num-1)
        
        return count
        