class Stack:
    def __init__(self):
        self.main = []

    def push(self, x):
        self.main.insert(0, x)

    def pop(self):
        del self.main[0]
        return self.main[0]

    def clear(self):
        self.main = []

    def __len__(self):
        return len(self.main)


zbb_var_dic = { "temp_shell_para" : '',
                "temp_calc" : '0' ,
                "temp_para": Stack(),
                "temp_ret": Stack(),
                "temp_all": Stack()
                }

"""
初始化了临时存储器
- 临时存储器tsp用于在shell中传递参数
- 临时存储器tc用于储存计算参数
- 临时存储器tp用于储存函数参数
- 临时存储器tr用于储存函数返回值
- 临时存储器ta是通用寄存器
"""
code_text_to_list = []
isJUMP = False