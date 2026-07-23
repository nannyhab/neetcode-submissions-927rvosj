class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       hashMap = {}

       for string in strs:
        stringSorted = "".join(sorted(string)) 
        if stringSorted in hashMap:
            hashMap[stringSorted].append(string)
        else:
            hashMap[stringSorted] = [string]
       results = []
       for values in hashMap.values():
        results.append(values) 
       return results

