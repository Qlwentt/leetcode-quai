class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        def count_execute(start_r, start_c, instructions):
            r = start_r
            c = start_c
            count = 0
            while instructions:
                command = instructions.popleft()
                if command == "U":
                    r -= 1
                elif command == "D":
                    r += 1
                elif command == "L":
                    c -= 1
                else:
                    c += 1
                if r not in range(n) or c not in range(n):
                    break
                count += 1
            return count
        answer = [0] * len(s)
        
        for i in range(len(answer)):
            instr = collections.deque(list(s[i:]))
            answer[i] = count_execute(startPos[0], startPos[1], instr)
        return answer