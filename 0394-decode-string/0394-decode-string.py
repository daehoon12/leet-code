class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        curr_num = 0
        answer = []
        curr_str = ''
        for c in s:
            if c.isdigit():
                curr_num = curr_num*10 + int(c)
            else:
                if c == '[':
                    st.append((curr_str, curr_num))
                    curr_num = 0
                    curr_str = ''
                elif c == ']':
                    prev_str, num = st.pop()
                    curr_str =prev_str + curr_str*num
                else:
                    curr_str += c        
        return curr_str
                