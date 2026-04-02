class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        list_of_dicts = dict()

        for string in strs:
            
            key = ''.join(sorted(string))

            if key not in list_of_dicts:
                list_of_dicts[key] = []
            list_of_dicts[key].append(string)

        return list(list_of_dicts.values())