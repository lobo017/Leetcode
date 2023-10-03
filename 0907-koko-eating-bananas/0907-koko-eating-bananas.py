class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 1
        ans = r
        for pile in piles:
            r = max(r,pile)
        
        while(l<=r):
            mid = int(l+(r-l) / 2)
            if self.checkIfPossible(mid,piles,h):
                r = mid-1
                ans = mid
            else:
                l = mid + 1
        return ans

    def checkIfPossible(self, mid: int, piles: List[int], h:int):
        total_hours = 0
        for pile in piles:
            current_hours = int(pile / mid)
            if pile % mid != 0:
                current_hours +=1
            total_hours += current_hours
            if total_hours > h:
                return False
        return True

        