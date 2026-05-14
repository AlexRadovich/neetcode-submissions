class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,-1

        while(1):
            if numbers[l] + numbers[r] > target:
                r -=1
            elif numbers[l] + numbers [r] < target:
                l += 1
            else:
                return [l+1, r + 1 + len(numbers)]
