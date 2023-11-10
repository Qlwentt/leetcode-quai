class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        remainder = 0
        while digits or remainder:
            digit = digits.pop() if digits else 0
            add = (digit + remainder + (len(answer) == 0))
            newDigit = add % 10
            remainder = add // 10
            answer.append(newDigit)
        answer.reverse()
        return answer
        
            