class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set() 
        setB = set()
        common = 0
        answer = [0]* len(A)
        for i,(a,b) in enumerate(zip(A,B)):
            setA.add(a)
            setB.add(b)
            
            if b in setA:
                common += 1
            
            if a in setB and a != b:
                common += 1 
            answer[i] = common
        return answer