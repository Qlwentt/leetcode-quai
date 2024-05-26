class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        counts = collections.defaultdict(int)
        answer = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            key = tuple((size, counts[size]// size))
            counts[size] += 1
            answer[key].append(i)
            
        return answer.values()
        
    
            