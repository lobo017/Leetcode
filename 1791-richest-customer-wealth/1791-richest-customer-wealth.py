class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        
        for account in accounts:
            partSum = 0
            for i in range(len(account)):
                partSum += account[i]
            wealth = max(wealth,partSum)
            
        return wealth