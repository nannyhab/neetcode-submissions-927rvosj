class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = 1
        result = nums[0]

        for index in range(1, len(nums)):
            if nums[index] != result and counter == 0:
                result = nums[index]
                counter = 1
            elif nums[index] != result:
                counter -= 1
            else:
                counter += 1
        
        return result

