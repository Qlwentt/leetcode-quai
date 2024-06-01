class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # [3,2,5,1,3,4]
        skill = sorted(skill)
        total_skill = skill[0] + skill[-1]
        
        sum_chemistry = 0
        
        L = 0
        R = len(skill) - 1
        
        while L < R:
            if skill[L] + skill[R] != total_skill:
                return -1
            sum_chemistry += skill[L] * skill[R]
            
            L += 1
            R -= 1
        
        return sum_chemistry