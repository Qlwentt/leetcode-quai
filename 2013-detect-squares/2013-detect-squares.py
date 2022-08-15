from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.pointsMap = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsMap[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        result = 0
        for x,y in self.points:
            if (abs(px - x) != abs(py-y) or px == x or py ==y):
                continue
            result += self.pointsMap[(x, py)] * self.pointsMap[(px, y)]
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)