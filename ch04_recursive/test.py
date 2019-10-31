def test01(S,n):
    """
    R-4.1 对于一个含有 n 个元素的序列 S，描述一个递归算法查找其最大值。
    :return:
    """
    if n == 0:
        return S[n]
    elif S[n-1] < S[n]:
        S[n-1]=S[n]
        return test01(S,n-1)

def test06(n):
    """
    R-4.6 描述一个递归函数，用于计算第 n 个调和数
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return 1/n + test06(n-1)

if __name__ == "__main__":
    S=[1,2,3]
    #print(test01(S,len(S)-1))
    print(test06(3))