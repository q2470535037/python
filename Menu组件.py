import tkinter # 导入tkinter模式
root = tkinter.Tk()
menu = tkinter.Menu(root) # 生成菜单
submenu = tkinter.Menu(menu, tearoff=0) # 生成下拉菜单
submenu.add_command(label = "Open") # 向下拉菜单中添加open命令
submenu.add_command(label = "Save") # 向下拉菜单中添加Save命令
submenu.add_command(label = "Close")# 向下拉菜单中添加Close命令
menu.add_cascade(label="File", menu=submenu) # 将下拉菜单中添加到菜单中
submenu = tkinter.Menu(menu, tearoff=0) # 生成下拉菜单
submenu.add_command(label = "Copy") # 向下拉菜单中添加Copy命令
submenu.add_command(label = "Paste") # 向下拉菜单中添加Paste命令
submenu.add_separator() # 向下拉菜单中添加分隔符
menu.add_cascade(label="Cut") # 向下拉菜单中添加Cut命令
submenu.add_command(label = "Exit", command=root.quit) # 将下拉菜单添加到菜单中
submenu = tkinter.Menu(menu, tearoff=0) # 生成下拉菜单
submenu.add_command(label = "About") # 向下拉菜单中添加About命令
menu.add_cascade(label="Help", menu=submenu) # 将下拉菜单添加到菜单中
root.config(menu=menu)
root.mainloop()