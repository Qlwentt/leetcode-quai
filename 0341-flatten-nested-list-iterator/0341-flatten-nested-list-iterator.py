# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        self.i = 0
        self.flatten(nestedList)
        
    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.flattened.append(item.getInteger())
            else:
                self.flatten(item.getList())
            
        
    
    def next(self) -> int:
        answer = self.flattened[self.i]
        self.i += 1
        return answer
        
    
    def hasNext(self) -> bool:
         return self.i in range(len(self.flattened))

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())