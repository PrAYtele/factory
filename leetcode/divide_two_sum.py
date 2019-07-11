def divide(dividend: int, divisor: int):
    sign = True if dividend^divisor>0 else False
    time = 0
    divisor,dividend = abs(divisor),abs(dividend)
    while dividend >= divisor:
        temp_divisor,count = divisor,1
        while dividend >= temp_divisor:
            dividend -= temp_divisor
            time += count
            count = count<<1
            temp_divisor = temp_divisor<<1
    time = time if sign == True else -time
    return time,dividend

def decimal(divisor,dividend):
    arr = []
    res = ''
    temp = dividend
    if temp == 0:
        return res
    while temp != 0:
        dividend,temp = divide(temp*10,divisor)
        if [dividend,temp] in arr:
            for i in range(len(arr)):
                res += str(arr[i][0])
            res = '('+res+')'
            return res
        arr.append([dividend,temp])
    for i in range(len(arr)):
        res += str(arr[i][0])
    return res
def main(dividend,divisor):
    point_left,mod = divide(dividend,divisor)
    point_right = decimal(divisor,mod)
    res = str(point_left) + '.'+ point_right
    return res
print(main(10,3))