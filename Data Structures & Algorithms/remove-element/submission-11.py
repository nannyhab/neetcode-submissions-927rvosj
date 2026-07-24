class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        kCount = 0
        writePtr = 0
        
        for readPtr in range(len(nums)):
            if nums[readPtr] == val:
                nums[readPtr] = "_"
            else:
                nums[writePtr] = nums[readPtr]
                writePtr += 1
                kCount += 1
        return kCount