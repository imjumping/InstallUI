import tkinter as tk
from tkinter import ttk
import random as rd
import os
print("库导入成功！")
###下面是一个UI，没啥用，所以如果想要当成一个应用程序的框架，就删掉下面的无用功
def start_move(event):
    global x, y
    x = event.x
    y = event.y

def stop_move(event):
    global x, y
    x = None
    y = None

def on_move(event, window):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    new_x = window.winfo_x() + deltax
    new_y = window.winfo_y() + deltay
    window.geometry(f"+{new_x}+{new_y}")

def add_progress(progress, window, current_value):
    if current_value[0] < 100:
        current_value[0] += 10
        progress["value"] = current_value[0]
        window.after(int(rd.random() * 1000), lambda: add_progress(progress, window, current_value))
    else:
        window.destroy()
    return current_value[0]

def create_window():
    global x, y
    x, y = 0, 0

    root = tk.Tk()
    root.title("安装界面")
    root.geometry("500x250")
    root.overrideredirect(True)

    root.bind("<ButtonPress-1>", start_move)
    root.bind("<ButtonRelease-1>", stop_move)
    root.bind("<B1-Motion>", lambda event: on_move(event, root))

    progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress.pack(pady=20)

    close_button = tk.Button(root, text="关闭", command=root.destroy)
    close_button.pack()

    current_value = [0]

    add_progress(progress, root, current_value)

    root.mainloop()

    return current_value[0]

final_value = create_window()
if final_value >= 100:
    print("进入安装程序")
    import installer as itr
else:
    exit()
###如果把它当成一个框架，请删掉上面代码
#import installer as itr
folder_loader = itr.select_folder()
print(folder_loader)
root2 = tk.Tk()
root2.title("提示！")
text2 = tk.Label(root2, text="开始安装！")
text2.pack()
button1 = tk.Button(root2, text="确定", command=root2.destroy)
button1.pack()
root2.geometry("300x100")
root2.bind("<ButtonPress-1>", start_move)
root2.bind("<ButtonRelease-1>", stop_move)
root2.bind("<B1-Motion>", lambda event: on_move(event, root2))
root2.mainloop()
files = os.listdir(folder_loader)


temp_dir = os.path.join(folder_loader, "install_temp")
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
else:
    print(f"创建成功。")

# 清空文件内容再写入
temp_file_path = os.path.join(temp_dir, "config.ini")
with open(temp_file_path, "w") as f:
    f.write("#安装程序配置config\n")

# 下面填入安装的应用的解压代码
pass