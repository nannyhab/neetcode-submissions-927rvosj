class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        bucketList = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        print(f"what hashmap looks like {hashMap}")

        for key, v in hashMap.items():
            bucketList[v].append(key)
        
        print(f"what bucketList looks like {bucketList}")

        result = []
        for i in range(len(bucketList)-1, 0, -1):
            for x in bucketList[i]:
                result.append(x)
                print(f"this is what result looks like {result}")
                print(len(result))
                if len(result) == k:
                    return result


            
        