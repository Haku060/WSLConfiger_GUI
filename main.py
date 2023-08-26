import os
from tkinter import *



def apply_config():
    global file_path
    global config
    file_path = file_path_Text.get(1.0, END).strip().encode()

    print(config)
    IPv6_State.get()
    with open('.wslconfig', 'w') as f:
        f.write(f'[wsl2]')
        for key, value in config.items():
            f.write(f'{key}={value}\n')

def do_file():
    pass


file_path = os.path.join(os.environ['USERPROFILE'], '.wslconfig')
config = {}
# 读取设置
with open(file_path, 'r') as f:
    lines = f.readlines()
for line in lines:
    if '=' in line:
        key, value = line.strip().split('=')
        config[key] = value


# 根窗口创建
root = Tk()

root.title("WSL Configer")
root.geometry("380x150")
Label(root, text="File Path").place(x=0, y=0)
file_path_Text = Text(root, width=45, height=1)
file_path_Text.insert(END, file_path)
file_path_Text.place(x=55, y=3)


IPv6_State = IntVar()
Checkbutton(root, text="IPv6", variable=IPv6_State).place(x=5, y=20)

apply_config_button = Button(root, text="应用设置", width=8, command=apply_config)
apply_config_button.place(x=10, y=75)
root.mainloop()
