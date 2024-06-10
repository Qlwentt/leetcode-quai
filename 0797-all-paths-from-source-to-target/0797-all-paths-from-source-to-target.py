class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = graph
        answer = []
        def dfs(node, path):
            if node is None:
                return
            if node == len(graph) - 1:
                path.append(node)
                answer.append(path.copy())
                return
            
            path.append(node)
            for neigh in adjList[node]:
                dfs(neigh,path.copy())
        dfs(0,[])
        return answer
            
        
        
        