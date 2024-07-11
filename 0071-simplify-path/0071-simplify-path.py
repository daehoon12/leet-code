class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = list(filter(lambda x: x != "", path.split("/")))

        stack = []
        for p in path_list:
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.':
                continue
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)