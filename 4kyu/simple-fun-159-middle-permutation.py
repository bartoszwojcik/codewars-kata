# Factoradic version

from math import factorial

def middle_permutation(string):
    sorted_s = sorted(list(string))
    middle = (factorial(len(string)) - 1) // 2

    factoradic = []

    i = 1
    while middle > 0:
        middle, modulo = middle // i, middle % i
        factoradic.append(modulo)
        i += 1

    output = ""
    for i in range(len(factoradic) - 1, -1, -1):
        output += sorted_s.pop(factoradic[i])

    return output


if __name__ == "__main__":
    print("abc:", middle_permutation("abc"))
    print("abcd:", middle_permutation("abcd"))
    print("abcdx:", middle_permutation("abcdx"))
    print("abcdxg:", middle_permutation("abcdxg"))
    print("abcdxgz:", middle_permutation("abcdxgz"))
    print(
        "qwertyuiopasdfghjklzxcvbnm:",
        middle_permutation("qwertyuiopasdfghjklzxcvbnm")
    )
