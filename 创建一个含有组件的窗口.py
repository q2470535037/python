import tkinter # 导入tkinter模块
root = tkinter.Tk() # 生成root窗口
label = tkinter.Label(root, text = "Hello,tkinter!") # 生成标签
label.pack() # 将标签添加到root窗口
button1 = tkinter.Button(root, text = "BUTTON1") # 生成button1
button1.pack(side = tkinter.LEFT) # 添加到root主窗口
button2 = tkinter.Button(root, text = "BUTTON2") # 生成button2
button2.pack(side = tkinter.RIGHT) # 将button2添加到root主窗口+
root.mainloop()