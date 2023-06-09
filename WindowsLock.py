import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# 基于tk实现的全屏锁屏应用

PASSWORD = "88888888"  # 设置解锁密码
BACKGROUND_IMAGE = "111.jpg"  # 设置背景图片
CONTACT_INFO = "请联系陈安帮"  # 设置联系信息

def check_password():
    entered_password = password_entry.get()
    if entered_password == PASSWORD:
        root.destroy()
    else:
        messagebox.showerror("错误", "密码错误！")

root = tk.Tk()
root.attributes("-fullscreen", True)  # 全屏显示
# root.config(cursor="none")  # 隐藏鼠标光标

# 设置背景图片
background_image = Image.open(BACKGROUND_IMAGE)
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# 创建输入框和按钮
password_entry = tk.Entry(root, show="*", font=("Helvetica", 24))
password_entry.place(relx=0.5, rely=0.5, anchor="center")
submit_button = tk.Button(root, text="确定", font=("Helvetica", 16), command=check_password)
submit_button.place(relx=0.5, rely=0.6, anchor="center")

# 创建联系信息标签
contact_label = tk.Label(root, text=CONTACT_INFO, font=("Helvetica", 16), bg="white")
contact_label.place(relx=0.5, rely=0.7, anchor="center")

# 禁用 Alt+F4 关闭程序
root.protocol("WM_DELETE_WINDOW", lambda: None)

root.mainloop()