class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for key, value in hashMap.items():
            bucket[value].append(key)
        
        topK = []
        for i in range(len(bucket)-1, 0, -1):
            for element in bucket[i]:
                topK.append(element)
                print(f"topK is {topK}")
                if len(topK) == k:
                    return topK
        