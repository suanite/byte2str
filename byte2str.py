#! /usr/bin/env python
# -*- coding:utf-8 -*-


from Tkinter import *
import re


class Byte2str(object):
    def __init__(self, master=None):
        self.flag = BooleanVar()

        self.byte_label = Label(master, text='字节流')
        self.str_label = Label(master, text='字符流')
        self.byte_text = Text(master, height=5, width=40)
        self.str_text = Text(master, height=5, width=40)
        self.byte2str_button = Button(master, text='====>', command=self.byte2str)
        self.str2byte_button = Button(master, text='<====', command=self.str2byte)
        self.character_checkbutton = Checkbutton(master, variable=self.flag, text='utf-8编解码', onvalue=True, offvalue=False)

        self.byte_label.grid(row=0, column=0, padx=5, sticky='w')
        self.str_label.grid(row=0, column=2, padx=5, sticky='w')
        self.byte_text.grid(row=1, column=0, rowspan=3, padx=5, pady=5, sticky='w')
        self.byte2str_button.grid(row=1, column=1)
        self.str2byte_button.grid(row=2, column=1)
        self.str_text.grid(row=1, column=2, rowspan=2, padx=5, pady=5, sticky='w')
        self.character_checkbutton.grid(row=4, column=0, sticky='w')

    def byte2str(self):
        byte_data = self.byte_text.get('1.0', 'end')
        byte_data = re.sub('[\n\r\t ]', '', byte_data).upper()

        base = '0123456789ABCDEF'  # 将字符转成对应的16进制数
        i = 0
        foo = ''
        while i < len(byte_data):
            c1 = byte_data[i]
            c2 = byte_data[i + 1]
            i += 2
            b1 = base.find(c1)
            b2 = base.find(c2)
            if b1 == -1 or b2 == -1:
                return None
            foo += chr((b1 << 4) + b2)

        if self.flag.get():
            str_data = foo.decode('utf-8', 'ignore')
        else:
            str_data = foo.decode('cp936', 'ignore')

        self.str_text.delete('1.0', 'end')
        self.str_text.insert('1.0', str_data)

    # 字符串转字节流还没实现
    def str2byte(self):
        foo = self.str_text.get('1.0', 'end')
        print(foo.decode('cp936'))


if __name__ == '__main__':
    root = Tk()
    app = Byte2str(root)
    root.resizable(False, False)
    root.mainloop()

