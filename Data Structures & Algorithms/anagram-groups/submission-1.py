class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        the_dict = dict()

        for string in strs:

            key = ''.join(sorted(string))

            if key not in the_dict:
                the_dict[key] = []
            the_dict[key].append(string)
        
        return list(the_dict.values())
        