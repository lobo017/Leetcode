class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        res = []
        for i in range(len(digits)):
            num += str(digits[i])
        num = str(int(num) + 1)
        
        for j in range(len(num)):
            res.append(int(num[j]))
        return res