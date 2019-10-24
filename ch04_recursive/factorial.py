# 4-1 阶乘函数的递归实现
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))