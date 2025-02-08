from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.container = collections.defaultdict(lambda: SortedSet())
        # number, indexes it is found at
        self.index_to_number = {}
        

    def change(self, index: int, number: int) -> None:
        current_number_at_index = self.index_to_number.get(index, None)
        if current_number_at_index != None:
            self.container[current_number_at_index].remove(index)
        self.container[number].add(index)
        self.index_to_number[index] = number

    def find(self, number: int) -> int:
        return self.container[number][0] if self.container[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)