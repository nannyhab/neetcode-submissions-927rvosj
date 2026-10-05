class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashMap = {0:1}

        counter = 0
        currentSum = 0

        for num in nums:
            currentSum += num
            pastSum = currentSum - k
            if pastSum in hashMap:
                counter += hashMap[pastSum]
            hashMap[currentSum] = hashMap.get(currentSum,0) + 1
        
        return counter
