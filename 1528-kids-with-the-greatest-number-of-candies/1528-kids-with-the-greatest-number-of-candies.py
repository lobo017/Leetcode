class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # candies = [2,3,5,1,3]
        # kids = [5,6,8,4,6]

        ans = []

        kids = []
        for x in candies:
            kids.append(x+extraCandies)

        count = 0

        for i in range(len(kids)):
            for j in range(len(candies)):
                if kids[i] >= candies[j]:
                    count += 1
                else:
                    break
            ans.append(count == len(kids))
            count = 0

        return ans       