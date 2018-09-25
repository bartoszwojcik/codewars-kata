from math import log

def isPP(n):

    def primes(maximum):
        possible = []
        for i in range(2, maximum + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                possible.append(i)
        return possible

    for k in primes(int(log(n, 2))):

        i = 1
        while i ** k <= n:
            if i ** k == n:
                return [i, k]
            i += 1

    return None

if __name__ == "__main__":
    print(isPP(10))
    print(isPP(5))
    print(isPP(4))
    print(isPP(9))
    print(isPP(484))
