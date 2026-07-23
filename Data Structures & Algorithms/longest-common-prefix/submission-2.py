class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longestCommonPrefix = ""
        for index in range(len(strs[0])):
            currentChar = strs[0][index]
            for string in strs:
                if index == len(string) or string[index] != currentChar:
                    return longestCommonPrefix
            longestCommonPrefix+=currentChar
            
        return longestCommonPrefix
        