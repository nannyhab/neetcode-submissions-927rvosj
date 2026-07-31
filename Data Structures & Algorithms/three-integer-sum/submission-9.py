class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [] 
        
        for i,e in enumerate(nums):

            if i > 0 and e == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                threeSum = nums[L] + nums[R] + e
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    result.append([e, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return result


