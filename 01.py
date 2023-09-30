import tkinter as tk
import random
import pyttsx3 as pt
import json
engine = pt.init()
a = []
cc = 0
with open('000.txt', 'r', encoding='utf-8') as f:
    for ann in f.readlines():
        ann = ann.strip('\n')
        a.append(ann)
def gx():
    x = random.randint(0, int(len(a) - 1))
    l.config(text=a[x])
    with open('000.json', 'r+', encoding='utf-8') as f:
        content = f.readline()
        if content == '1':
            engine.say(a[x])
            engine.runAndWait()
        else:
            pass
def gy():
    def s():
        with open('000.json', 'r+', encoding='utf-8') as f:
            content = f.readline()
            if content == '1':
                tm.config(text="当前为朗读")
            else:
                tm.config(text="当前为不朗读")
    def f():
        with open('000.json', 'r+', encoding='utf-8') as f:
            content = f.readline()
            if content == '1':
                with open('000.json', 'w', encoding='utf-8') as f:
                    f.write('0')
                    f.close()
            else:
                with open('000.json', 'w', encoding='utf-8') as f:
                    f.write('1')
                    f.close()
        print('Modified the file successfully.')
        s()
    qt = tk.Tk()
    qt.geometry("60x80")
    t = tk.Label(qt,text="点名器2.11\n是否朗读")
    t.pack()
    tm = tk.Button(qt, text="0", command=f)
    tm.pack()
    qt.mainloop()
dm = tk.Tk()
dm.title("点名器2.11")
dm.geometry('160x80')
l = tk.Label(dm,text="点名器2.11",font=("楷体",14),fg="red")
l.pack()
bu = tk.Button(dm,text="抽取",command=gx)
bu.pack()
guanyv = tk.Button(dm,text="关于",command=gy)
guanyv.pack()
dm.mainloop()
#本品由@不知织梦...制件")