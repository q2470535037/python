import tkinter
from tkinter.messagebox import *
resule = askretrycancel(title='请确认8',message='操作失败')
if resule == True:
    showinfo(title='提示',message='已经重试')
else:
    showerror(title='提示',message='取消重试')