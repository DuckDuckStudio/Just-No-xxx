import tkinter as tk
from PIL import ImageTk, Image

# 创建Tkinter窗口
root = tk.Tk()
root.attributes("-fullscreen", True)

# 加载图片
image_path = ".\\Blue screen of death.png"
image = Image.open(image_path)
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # 调整图片大小以适应屏幕
photo = ImageTk.PhotoImage(image)

# 在窗口中显示图片
label = tk.Label(root, image=photo)
label.pack(fill="both", expand=True)

# 关闭窗口的函数
def close_window(event=None):
    root.destroy()

# 关闭窗口的快捷键
root.bind("<Escape>", close_window)

root.mainloop()
