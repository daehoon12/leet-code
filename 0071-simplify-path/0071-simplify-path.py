class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        path_list = path.split("/")

        for p in path_list:
            if answer and p == '..':
                answer.pop()
            if p not in ['.', '..', '']:
                answer.append(p)
        return "/" + "/".join(answer)