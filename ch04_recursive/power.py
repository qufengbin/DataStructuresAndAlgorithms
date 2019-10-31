def power(x,n):
    """
    用简单的递归计算幂函数
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)

def power2(x,n):
    """
    使用重复的平方根计算幂函数
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        partial = power2(x,n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result