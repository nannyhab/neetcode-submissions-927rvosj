class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L = i+1
            R = len(nums) - 1

            while L < R:
                sum3 = a + nums[L] + nums[R]
                if sum3 > 0:
                    R -= 1
                elif sum3 < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L+=1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        return res

        


        