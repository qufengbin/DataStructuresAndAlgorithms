def binary_search(data,target,low,high):
    """
    使用递归实现二分查找算法
    二分查找：该算法用于在一个含有 n 个元素的有序序列中有效地定位目标值。
    """
    if low > high:
        print("{}不存在".format(target))
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            print("data[{}]为{}".format(mid,target))
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid - 1)
        else:
            return binary_search(data,target,mid + 1,high)

if __name__ == "__main__":
    test = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
    binary_search(test,30,0,len(test)-1)