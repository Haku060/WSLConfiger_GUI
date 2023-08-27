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

style = Style(theme='minty')
root = style.master

root.title("WSL Configer")
root.geometry("380x320")
Label(root, text="NetWork Relevant",font="微软雅黑 15").pack(side='top', anchor='nw',padx=5, pady=5)


# NetWork Relevant
IPv6_State = IntVar(value=1) if config['ipv6'] == 'true' else IntVar(value=0)
Checkbutton(root, text="IPv6", variable=IPv6_State).place(x=10,y=50)

Local_State = IntVar(value=1) if config['localhostForwarding'] =='true' else IntVar(value=0)
Checkbutton(root, text="localhostForwarding", variable=Local_State).place(x=200,y=50)

Frame(relief="flat").pack(fill="x", padx=5, pady=10)

Label(root, text="networkingMode").place(x=10,y=80)
networking_Mode_Text = Text(root, width=10, height=1)
networking_Mode_Text.insert(END, config['networkingMode'])
networking_Mode_Text.place(x=120,y=80)

Label(root, text="vmSwitch").place(x=10,y=110)
vmSwitch_Text = Text(root, width=10, height=1)
vmSwitch_Text.insert(END, config['vmSwitch'])
vmSwitch_Text.place(x=120,y=110)

Frame(relief="flat").pack(fill="x", padx=5, pady=40)

Label(root, text="Kernel Relevant",font="微软雅黑 15").pack(side='top', anchor='w',padx=5, pady=5)
Label(root, text="Memory").place(x=10,y=200)
memory_Text = Text(root,width=10,height=1)
memory_Text.insert(END,config['memory'])
memory_Text.place(x=120,y=200)

Label(root,text="Swap").place(x=10,y=230)
swap_Text = Text(root,width=10,height=1)
swap_Text.insert(END,config['swap'])
swap_Text.place(x=120,y=230)

Frame(relief="flat").pack(fill="x", padx=5, pady=10)

apply_config_button = Button(root, text="应用设置", width=8, command=apply_config)
apply_config_button.pack(side='bottom', anchor='se',padx=25, pady=25)
root.mainloop()
