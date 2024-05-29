class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        counts = defaultdict(int) 
        common = 0
        answer = [0]* len(A)
        for i,(a,b) in enumerate(zip(A,B)):
            counts[a] += 1
            counts[b] += 1
            if a == b:
                common += 1
            else:
                if counts[a] > 1:
                    common += 1
            
                if counts[b] > 1:
                    common += 1
            
            answer[i] = common
        return answer