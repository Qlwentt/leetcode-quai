class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        answer = []
        
        for numerator in range(1, n):
            denominator = n
            while denominator:
                if (numerator / denominator) < 1 and math.gcd(numerator, denominator) == 1:
                    answer.append(f'{numerator}/{denominator}')
                denominator -= 1
        return answer
            
        