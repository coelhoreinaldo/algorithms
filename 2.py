import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isInFibonacci(n):
    if n < 0:
        return False
    return isPerfectSquare(5 * (n**2) + 4) or isPerfectSquare(5 * (n**2) - 4)


numero = int(input("Informe um número: "))

if __name__ == "__main__":
    if isInFibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
