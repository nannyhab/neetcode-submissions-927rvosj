class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for string in strs:
            barCode = [0] * 26
            for char in string:
                charIndex = ord(char) - ord("a")
                barCode[charIndex] += 1
            barCode = tuple(barCode)
            if barCode in hashMap:
                hashMap[barCode].append(string)
            else:
                hashMap[barCode] = [string]
        finalList = []
        for value in hashMap.values():
            finalList.append(value)
        return finalList
            
