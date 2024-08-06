class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        
        for s in strs:
            encoding = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
            for char in s:
                encoding[char] += 1
            groups[tuple(encoding.items())].append(s)
        return groups.values()