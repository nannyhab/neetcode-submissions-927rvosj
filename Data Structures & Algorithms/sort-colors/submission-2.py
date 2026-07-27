class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0 for i in range(3)]


        for index in range(len(nums)):
            if nums[index] == 0:
                bucket[0]+=1
            elif nums[index] == 1:
                bucket[1]+=1
            else:
                bucket[2]+=1
        
        index = 0
        for color in range(3):
            for _ in range(bucket[color]):
                nums[index] = color
                index += 1
                
        return nums
