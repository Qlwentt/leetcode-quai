class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        sources = set([source for source, destination in paths])
        destinations = set([destination for source, destination in paths])
        
        for dest in destinations:
            if dest not in sources:
                return dest
        
        