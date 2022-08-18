class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [num%60 for num in time]
        complements = {}
        count = 0
        for num in time:
            comp = (60 - num) % 60
            if comp in complements:
                count += complements[comp]
            complements[num] = complements.get(num, 0) + 1
                        
        return count