def reverse(S,start,end):
    """
    使用线性递归逆置序列的元素
    :param S:
    :param start:
    :param end:
    :return:
    """
    if start < end-1:
        S[start],S[end-1] = S[end-1],S[start]
        reverse(S,start+1,end-1)

if __name__ == "__main__":
    S = [1,2,3,4,5,6,7,8]
    reverse(S,0,len(S))
    print(S)