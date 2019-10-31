import os

def disk_usage(path):
    """
    返回目录下所有文件和目录的大小，单位为 bytes
    :param path:
    :return:
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path.filename)
            total += disk_usage(childpath)

    print ('{0:<7}'.format(total),path)
    return total