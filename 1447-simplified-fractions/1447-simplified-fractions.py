class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        answer = []
        fractions = set()
        
        for numerator in range(1, n):
            denominator = n
            while denominator:
                if (numerator / denominator) < 1 and (numerator/denominator) not in fractions:
                    answer.append(f'{numerator}/{denominator}')
                    fractions.add(numerator/denominator)
                    
                denominator -= 1
        return answer
            
        