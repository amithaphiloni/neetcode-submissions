class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)
        while low <= high:
            mid = (low + high)//2
            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid - 1) // mid 
            if hours_spent > h:
                low = mid + 1
            if hours_spent <= h:
                high = mid - 1
        return low

