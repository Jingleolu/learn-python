"""
8个苹果分成四组每组至少一个苹果有多少种方案
8个苹果一共有7块挡板，插3块就行，组合的方式
C37
函数的重要性
"""


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


m = int(input("m="))
n = int(input("n="))
print(factorial(m) // factorial(n) // factorial(m-n))
