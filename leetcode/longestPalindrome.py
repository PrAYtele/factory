class Solution:
    def longestPalindrome(self, s: str) -> str:
        def centre(s,i,j):
            if len(s)==1:
                return 0,0

            while i>0 and j+1<len(s) and s[i] == s[j]:
                if s[i-1] == s[j+1]:
                    i-=1
                    j+=1
                else:
                    break
            return i,j
        start = 0
        end = 0
        for i in range(len(s)-1):
            a,b = centre(s,i,i)
            if (b-a)>(end-start) and s[a] == s[b]:
                start,end = a,b
            a,b = centre(s,i,i+1)
            if (b - a) > (end - start) and s[a] == s[b]:
                start, end = a, b
        return (s[start:end+1])
a = Solution()
print(a.longestPalindrome('abccbahjghjghjgnbbbbbnhjhj'))