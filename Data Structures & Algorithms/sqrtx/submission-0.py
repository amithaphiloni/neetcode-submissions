class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = 0 , x 
        while low<=high:
            mid = (low + high) // 2
            sqr = mid*mid
            if sqr == x:
                return mid
            if sqr < x:
                low = mid + 1
            if sqr > x:
                high = mid - 1
        return high