import tkinter # 导入tkinter模块
root = tkinter.Tk()
r = tkinter.StringVar() # 使用stringvar生成字符串变量用于单选框组件
r.set('1') # 初始化变量值
radio = tkinter.Radiobutton(root, # 生成单选框组件
                            variable=r, # 设置单选框关联的变量
                            value='1', # 设置选中单选框十其所关联的变量值，即r的值
                            text='张三') # 设置单选框显示的文本
radio.pack()
radio = tkinter.Radiobutton(root,
                             variable=r,
                             value='2', # 当选中该单选框时，r的值将被设置为'2'
                             text='李四')
radio.pack()
radio = tkinter.Radiobutton(root,
                            variable=r,
                            value='3',# 当选中该单选框时，r的值将被设置为'3'
                            text='王五')
radio.pack()
radio = tkinter.Radiobutton(root,
                            variable=r,
                            value='4',# 当选中该单选框时，r的值将被设置为'4'
                            text='赵六')
radio.pack()
c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root,
                            text='姓   名', # 设置复选框的文本
                            variable=c, # 设置复选框关联的变量
                            onvalue=1, # 当选中复选框时，c的值将被设置为'1'
                            offvalue=2)# 当选中复选框时，c的值将被设置为'2'
check.pack()
root.mainloop()
