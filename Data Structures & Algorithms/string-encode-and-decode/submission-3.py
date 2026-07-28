class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        index = 0
        while index < len(s):
            
            stringLength = ''
            while s[index] != '#':
                stringLength += s[index]
                index+=1
            
            stringLength = int(stringLength)

            index+=1 #skip the delimiter
            count = 0
            word = ''
            while count < stringLength:
                word += s[index]
                count += 1
                index += 1

            result.append(word)
        return result



