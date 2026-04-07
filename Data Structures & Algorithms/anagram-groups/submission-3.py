class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for string in strs:
            strSorted = ''.join(sorted(string))
            if strSorted not in hashMap:
                hashMap[strSorted] = [string]
            else:
                hashMap.get(strSorted).append(string)
        output = []
        for x in hashMap.values():
            output.append(x)
        return output

