class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights) , sum(weights)
        while low <= high:
            mid = (high + low) // 2
            days_needed = 1
            ship_w = 0
            for weight in weights:
                if ship_w + weight > mid:
                    days_needed += 1
                    ship_w = weight
                else:
                    ship_w += weight
            if days_needed > days:
                low = mid + 1
            else:
                high = mid - 1
                
        return low