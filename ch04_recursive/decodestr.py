# import sys
# path = sys.argv[1]
# with open(path,encoding='utf-8') as file:
#     line = file.readline()
#     while line:
#         str1 = line.split('\t')
#         str1[4] = str1[4].decode('unicode_escape')
#         print(' '.join(str1))

str1 = '20191001	all	图文	all	\u9b54\u9053\u7956\u5e08\u4e2d\uff0c\u90a3\u4e9b\u4e0d\u4e3a\u4eba\u77e5\u7684\u5c0f\u79d8\u5bc6\uff01	1607479233841938	9227557851727258216   15	7.5'
str2 = str1.split('\t')
print (str2[4])