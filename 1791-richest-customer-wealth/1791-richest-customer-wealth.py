class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = []
        
        for account in accounts:
            partSum = 0
            for i in range(len(account)):
                partSum += account[i]
            sums.append(partSum)
            
        wealth = -1
        for j in range(len(sums)):
            wealth = max(wealth,sums[j])
            
        return wealth