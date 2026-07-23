class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPrefix = ""

        for index in range(len(strs[0])):
            for string in strs:
                if index == len(string) or strs[0][index] != string[index]:
                    return longestCommonPrefix
            longestCommonPrefix += string[index]
        return longestCommonPrefix  