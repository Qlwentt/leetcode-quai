class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        # [1,4,3,2] energy  1
        # [2,6,3,1] experience 15
        add = 0
        curEnergy = initialEnergy
        curExperience = initialExperience
        for opponentEnergy, opponentExperience in zip(energy, experience):
            add += (opponentEnergy + 1) - curEnergy if (opponentEnergy + 1) - curEnergy > 0 else 0
            add += (opponentExperience + 1) - curExperience if (opponentExperience + 1) - curExperience > 0 else 0
            curEnergy += (opponentEnergy + 1) - curEnergy if (opponentEnergy + 1) - curEnergy > 0 else 0
            curExperience += (opponentExperience + 1) - curExperience if (opponentExperience + 1) - curExperience > 0 else 0
            curEnergy -= opponentEnergy
            curExperience += opponentExperience
        return add
            