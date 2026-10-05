class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        counter = 0
        currSum = 0

        for index in range(len(nums)):
            currSum += nums[index]
            prevSum = currSum - k

            if prevSum in hashMap:
                counter += hashMap[prevSum]
            
            hashMap[currSum] = hashMap.get(currSum, 0) + 1
        
        return counter
            

