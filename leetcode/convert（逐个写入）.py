class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def arr(s,n):
            if n == 1:
                return s
            flag = True
            array = [[] for i in range(n)]
            for j in range(len(s)):
                if j%(n-1) != 0 and flag == True:
                    array[n-1-j%(n-1)].append(s[j])
                if j%(n-1) != 0 and flag == False:
                    array[j%(n-1)].append(s[j])
                if j%(n-1) == 0:
                    if flag == True:
                        array[0].append(s[j])
                    if flag == False:
                        array[n-1].append(s[j])
                    flag = not flag
            return array
        if numRows == 1:
            return s
        else:
            new_array = []
            array = arr(s,numRows)
            for i in range(len(array)):
                new_array = new_array + array[i]
            return(''.join(new_array))
sol = Solution()
print(sol.convert("kllozdbndjizayyrljxrfofvyiylqqlbbypcbtqeeydgwdykpvbwmhrkrpwifjljjcllxbrbcxkacikrfmqrvjemzcugnfrw",91))