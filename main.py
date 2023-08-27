import os
from tkinter import *
from ttkbootstrap import Style


def apply_config():
    global file_path
    global config
    # file_path = file_path_Text.get(1.0, END).strip().encode()
    config['ipv6'] = 'true' if IPv6_State.get() else 'false'
    config['localhostForwarding'] = 'true' if Local_State.get() else 'false'
    config['networkingMode']=networking_Mode_Text.get(1.0, END).strip()
    config['vmSwitch'] = vmSwitch_Text.get(1.0, END).strip()
    config['memory'] = memory_Text.get(1.0, END).strip()
    config['swap'] = swap_Text.get(1.0, END).strip()
    print(config)
    with open(file_path, 'w') as f:
        f.write(f'[wsl2]\n')
        for key, value in config.items():
            f.write(f'{key}={value}\n')


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

style = Style(theme='darkly')
root = style.master

root = Tk()

root.title("WSL Configer")
root.geometry("380x250")
Label(root, text="NetWork Relevant").place(x=0, y=0)
# file_path_Text = Text(root, width=45, height=1)
# file_path_Text.insert(END, file_path)
# file_path_Text.place(x=55, y=3)

# NetWork Relevant
IPv6_State = IntVar()
Checkbutton(root, text="IPv6", variable=IPv6_State).place(x=5, y=20)

Local_State = IntVar()
Checkbutton(root, text="localhostForwarding", variable=Local_State).place(x=5, y=40)

Label(root, text="networkingMode").place(x=75, y=20)
networking_Mode_Text = Text(root, width=10, height=1)
networking_Mode_Text.insert(END, config['networkingMode'])
networking_Mode_Text.place(x=182, y=23)

Label(root, text="vmSwitch").place(x=182, y=40)
vmSwitch_Text = Text(root, width=10, height=1)
vmSwitch_Text.insert(END, config['vmSwitch'])
vmSwitch_Text.place(x=242, y=43)

Label(root, text="Kernel Relevant").place(x=0, y=70)
Label(root, text="Memory").place(x=5, y=93)
memory_Text = Text(root, width=10, height=1)
memory_Text.insert(END, config['memory'])
memory_Text.place(x=75, y=93)

Label(root, text="Swap").place(x=200, y=93)
swap_Text = Text(root, width=10, height=1)
swap_Text.insert(END, config['swap'])
swap_Text.place(x=242, y=93)

apply_config_button = Button(root, text="应用设置", width=8, command=apply_config)
apply_config_button.place(x=10, y=155)
root.mainloop()
