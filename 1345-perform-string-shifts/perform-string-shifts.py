class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            normalized_amount = amount % len(s)
            pivot = normalized_amount if direction == 0 else -normalized_amount 
            left = s[:pivot]
            right = s[pivot:]
            s = right + left
        return s