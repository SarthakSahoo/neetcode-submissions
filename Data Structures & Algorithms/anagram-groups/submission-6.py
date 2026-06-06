class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in dict1:
                dict1[key] = [string]
            else:
                dict1[key].append(string)
        return list(dict1.values())