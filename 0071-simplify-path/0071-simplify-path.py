class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        path = [item for item in path if item != ""]
        
        for item in path:
            if item == ".":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
                
        return "/" + "/".join(stack)