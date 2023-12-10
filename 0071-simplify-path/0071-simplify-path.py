import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.split("/+", path)
        path = list(filter(None, path))
        stack = []
        for directory in path:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == ".":
                pass
            else:
                stack.append(directory)
                
        return "/" + "/".join(stack)