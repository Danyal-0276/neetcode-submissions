class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}

        for i in range(len(nums)):
            temp = nums[i]
            t = target - temp
            if t in freq:
                return [freq[t], i]

            freq[temp] = i
        return []
