class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or not directory:
                continue
            else:
                stack.append(directory)
                
        return "/" + "/".join(stack)

# Time: O(N)
# Space: O(N)