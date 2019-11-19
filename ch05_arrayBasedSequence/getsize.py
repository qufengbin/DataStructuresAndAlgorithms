import sys

def getsize(n):
    data = []
    for k in range(n):
       a = len(data)
       b = sys.getsizeof(data)
       print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
       data.append(None)

if __name__=="__main__":
    getsize(26)

# 输出
# Length:   0; Size in bytes:   36
# Length:   1; Size in bytes:   52
# Length:   2; Size in bytes:   52
# Length:   3; Size in bytes:   52
# Length:   4; Size in bytes:   52
# Length:   5; Size in bytes:   68
# Length:   6; Size in bytes:   68
# Length:   7; Size in bytes:   68
# Length:   8; Size in bytes:   68
# Length:   9; Size in bytes:  100
# Length:  10; Size in bytes:  100
# Length:  11; Size in bytes:  100
# Length:  12; Size in bytes:  100
# Length:  13; Size in bytes:  100
# Length:  14; Size in bytes:  100
# Length:  15; Size in bytes:  100
# Length:  16; Size in bytes:  100
# Length:  17; Size in bytes:  136
# Length:  18; Size in bytes:  136
# Length:  19; Size in bytes:  136
# Length:  20; Size in bytes:  136
# Length:  21; Size in bytes:  136
# Length:  22; Size in bytes:  136
# Length:  23; Size in bytes:  136
# Length:  24; Size in bytes:  136
# Length:  25; Size in bytes:  136