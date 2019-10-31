def linear_sum(S,n):
    """
    使用线性递归计算序列元素的和
    :param S:序列
    :param n:序列的长度
    :return:
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S,n-1) + S[n-1]

if __name__=="__main__":
    test=[1,2,3,4,5,6,7,8,9]
    print(linear_sum(test,len(test)))