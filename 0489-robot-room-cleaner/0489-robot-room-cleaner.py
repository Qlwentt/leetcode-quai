# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [[-1,0], [0,1], [1,0], [0,-1]]
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(r,c, direction):
            visited.add((r,c))
            robot.clean()
            
            for i in range(4):
                newDirection = (direction + i) % 4
                dr, dc = directions[newDirection]
                newR = dr + r
                newC = dc + c
                if (newR,newC) not in visited and robot.move():
                    dfs(newR,newC, newDirection)
                    goBack()
                robot.turnRight()
        dfs(0,0,0)
        
            
        