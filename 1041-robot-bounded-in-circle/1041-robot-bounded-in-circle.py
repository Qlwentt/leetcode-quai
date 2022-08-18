class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        direction = 0 #0 is north, 1 is east, 2 is south, 3 is west
        for _ in range(4):
            for instruction in instructions:
                if instruction == "L":
                    direction = (direction + 1) % 4
                elif instruction == "R":
                    direction = (direction - 1) % 4
                elif instruction == "G":
                    if direction == 0:
                        y += 1
                    elif direction == 1:
                        x += 1
                    elif direction == 2:
                        y -= 1
                    elif direction == 3:
                        x -= 1
        return x == 0 and y == 0