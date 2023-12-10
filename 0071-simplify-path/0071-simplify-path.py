import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        # path = re.split("/+", path)
        # path = list(filter(None, path))
        stack = []
        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or not directory:
                pass
            else:
                stack.append(directory)
                
        return "/" + "/".join(stack)