class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {"+", "-", "*", '/'}
        for token in tokens:
            if token not in operators:
                st.append(int(token))
            else:
                second = st.pop()
                first = st.pop()
                
                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    result = int(math.trunc(first / second))
                st.append(result)
        return st[-1]