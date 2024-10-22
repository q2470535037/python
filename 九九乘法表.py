i = 1 # 起始的行数
while i<10:
    j = 1 # 起始的列表
    while j <= i:
        print("%d*%d = %d"%(j,i,j*i),end = ' ') #输出每行的乘法口诀
        j += 1 #增加列数
    print("") # 进行换行
    i += 1