class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a,b,c])
        a_to_b = (b-a-1)
        c_to_b = (c-b-1)
        max_ = (c-b-1) + (b-a-1)
        if a_to_b == 0 and c_to_b == 0:
            min_ = 0
        elif a_to_b <= 1 or c_to_b <= 1:
            min_ = 1
        else:
            min_ = 2
        return [min_,max_]