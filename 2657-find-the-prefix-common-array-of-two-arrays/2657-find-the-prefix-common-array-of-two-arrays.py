class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        answer = [0]* len(A)
        for i,(a,b) in enumerate(zip(A,B)):
            set1.add(a)
            set2.add(b)
            answer[i] = len(set1.intersection(set2))
        
        return answer