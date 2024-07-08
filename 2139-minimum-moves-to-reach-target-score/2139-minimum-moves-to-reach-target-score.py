class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = target
        moves = 0
        while n != 1:
            if n % 2 == 0 and maxDoubles:
                n = n // 2
                maxDoubles -= 1
                moves += 1
            else:
                if maxDoubles:
                    n -= 1
                    moves += 1
                else:
                    moves += n - 1
                    break
        return moves
                    