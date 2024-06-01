class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        answer = 0
        rungs = [0] + rungs
        for i in range(len(rungs)-1):
            cur_dist = rungs[i+1] - rungs[i]
            if cur_dist > dist:
                answer += (cur_dist - 1) // dist
        
        return answer