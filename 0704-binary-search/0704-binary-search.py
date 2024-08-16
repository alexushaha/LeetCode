class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while(left < right):
            mid = left + math.floor(left+right)
            if(target < nums[mid]):
                right = mid - 1
            else:
                left = mid
        return left if nums[left] == target else -1