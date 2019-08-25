class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        res = []
        result = 0
        if temp == 0:
            return result
        if temp < 0:
            temp = temp * -1
            flag = True
        while temp > 10:
            mod = int(temp % 10)
            res.append(mod)
            temp = (temp-mod)/10
        res.append(int(temp))
        for v in res:
            result = result * 10 + v
        if flag:
            result = result * -1
        return result
sol = Solution()
print(sol.reverse(-321))