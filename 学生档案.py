print('-------原有学生档案--------')
f = open('dossier.txt','r') # 以只读模式打开文件dossier.txt
content = f.read() # 读取原有学生档案
print(content) # 显示原有的学生档案信息
f.close()
print('-------添加学生档案--------')
while True:
    f = open('dossier.txt','a') # 以追加模式打开学生档案文件dossier.txt
    name = input('请输入学生姓名(退出，输入q或Q):')
    if name == 'q'or name == 'Q': #判断用户是否进行了退出
        f.close()
        break
    else: # 用户没有进行退出，则添加档案信息
        ID = input('请输入身份证号:')
        f.write(name) # 添加新来学生的档案信息————姓名
        f.write('\t')
        f.write(ID) # 添加新来学生的档案信息————身份证号
        f.write('\n')
        f.close()
print('-------现有学生-------')
f = open('dossier.txt','r')
content = f.read()
print(content) # 显示最终的学生档案信息
f.close()