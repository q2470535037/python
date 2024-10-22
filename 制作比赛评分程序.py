list = []
for i in range(1, 11):
    print('第',i,'个评委打分：',end = '')
    score = int(input())
    list.append(score)
min = min(list)
max = max(list)
print('去掉一个最低分',min)
list.remove(min)
print('去掉一个最高分',max)
list.remove(max)
average = sum(list)/len(list)
print('该选手最终得分：',average)