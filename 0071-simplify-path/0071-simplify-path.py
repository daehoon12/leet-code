class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = [p for p in path.split("/") if p]

        stack = []
        for p in path_list:
            if p == '..':
                if stack:
                    stack.pop()
            elif p != '.':
                stack.append(p)
        
        return "/" + "/".join(stack)
