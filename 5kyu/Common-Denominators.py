from math import gcd

def convertFracts(lst):
    if len(lst) < 2:
        return lst

    output = lst[:]

    def lcm(num1, num2):
        return num1 * (num2 // gcd(num1, num2))

    def lcmm(lst):
        if len(lst) == 2:
            return lcm(lst[0][1], lst[1][1])
        else:
            return lcm(lst.pop(0)[1], lcmm(lst))

    lcd = lcmm(lst)

    for elem in output:
        elem[0] = int(elem[0] * (lcd // elem[1]))
        elem[1] = lcd

    return output


if __name__ == "__main__":
    a = [[1, 2], [1, 3], [1, 4]]
    print(convertFracts(a))

    a = [[4, 4], [2, 2], [1, 1]]
    print(convertFracts(a))

    a = [[2, 3]]
    print(convertFracts(a))

    a = [[4, 4], [2, 2], [1, 1], [2, 8], [3, 12553], [2, 15223]]
    print(convertFracts(a))
