# while中嵌入whlie进行表示
i = 0
while i <= 5: # 外循环
    print("上班星期为:",i)
    i = i+1
    t = 9
    while t <= 17: # 内循环
        print("时间段:",t)
        t = t+1
# while中嵌入for进行表示
while i <= 5: # 外循环
    print("上班星期为:",i)
    i = i+1
    for t in["9","10","11","12","13","14","15","16","17"]: # 内循环
        print("时间段：",t)
#for中嵌入for进行表示
for i in ["1","2","3","4","5"]: # 外循环
    print("上班星期为：",i)
    for t in ["9", "10", "11", "12", "13", "14", "15", "16", "17"]:  # 内循环
        print("时间段",i)
# for中嵌入while进行表示
for i in ["1","2","3","4","5"]: # 外循环
    print("上班星期为：",i)
    t = 9
    while t <= 17:
        print("时间段：",t)
        t = t+1