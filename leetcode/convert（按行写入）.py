class Solution:
    def convert(self,s,numRows):
        if numRows == 1:
            return s
        def arr(s,n):
            a = [[] for i in range(n)]
            for i in range(n):
                j = 0
                while (i + j)<len(s):
                    a[i].append(s[i+j])
                    if i%(n-1) != 0 and (j + 2*n-2 - i)<len(s):
                        a[i].append(s[j + 2*n-2 - i])
                    j+= (2*n-2)

            new_array = []
            for i in range(n):
                new_array = new_array + a[i]
            result = ''.join(new_array)
            return result
        return arr(s,numRows)
sol = Solution()
print(sol.convert('leetcodeabcd',5))