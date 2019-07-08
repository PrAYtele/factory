class solution:
    def longestsubstring (self,strr):
        dict = {}
        start = 0
        max_len = 0
        for i in range(len(strr)):
            if strr[i] in dict and dict[strr[i]] >= start:
                start = dict[strr[i]] + 1
            dict[strr[i]] = i
            current_len = i - start +1
            max_len = max(max_len,current_len)
        return max_len
a = solution()
print(a.longestsubstring('rrrrsdfaz'))