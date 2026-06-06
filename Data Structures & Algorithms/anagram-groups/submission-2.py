class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        dict1 = {}
        for string in strs:
            sorted_key = ''.join(sorted(string))
            if sorted_key not in dict1:
                dict1[sorted_key] = [string]
            else:
                dict1[sorted_key].append(string)
        for arr in dict1.values():
            groups.append(arr)
        return groups