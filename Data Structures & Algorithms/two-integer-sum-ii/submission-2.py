class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right , left = 0,len(numbers) - 1
        while left > right:
            if numbers[right] + numbers[left] == target:
                return [right + 1,left + 1]
            if numbers[right] + numbers[left] > target:
                left -= 1
            else:
                right+=1
        return -1
