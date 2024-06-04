class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i+1 for i in range(m)]
        answer = []
        for query in queries:
            i = P.index(query)
            answer.append(i)
            P.pop(i)
            P.insert(0,query)
        return answer
            