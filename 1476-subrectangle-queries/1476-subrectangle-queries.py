class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.rows = collections.defaultdict(lambda : collections.deque([])) #{0:[5], 1:[5], 2:[5], 3:[5,10]}
        self.cols = collections.defaultdict(lambda : collections.deque([])) # {0:[5,10], 1:[5,10], 2:[5,10]}
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            self.rows[i].appendleft(newValue) 
        for i in range(col1, col2+1):
            self.cols[i].appendleft(newValue)

    def getValue(self, row: int, col: int) -> int:
            row_updates = self.rows[row] 
            col_updates = set(self.cols[col])
            for update in row_updates:
                if update in col_updates:
                    return update
            return self.rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)