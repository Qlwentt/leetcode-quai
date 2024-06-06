class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev = 0
        answer = []
        for num in pref:
            next_ = prev ^ num
            prev = prev ^ next_
            answer.append(next_)
        
        return answer        