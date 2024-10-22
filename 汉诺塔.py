def move(N, A, B, C): #定义移动函数move()
    if N == 1:
        print(A, '-->',C)
    else:
        move(N-1, A, C, B) # 递归调用移动函数move()
        move(1, A, B, C)
        move(N-1, B, A, C)
num = input('请输入A柱圆盘的个数：')
num = int(num)
print('把A柱子上的',num,'个圆盘全部移动到C柱子的顺序为：')
move(num, 'A', 'B', 'C')