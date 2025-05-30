class Stack:
    def __init__(self):
        self.main = []

    def push(self, x):
        self.main.insert(0, x)

    def pop(self):
        if len(self.main) > 0:
            return self.main.pop(0)

    def clear(self):
        self.main = []

    def __len__(self):
        return len(self.main)

    def __repr__(self):
        return repr(self.main)

def between(var,a, b):
    return True if var.startswith(a) and var.endswith(b) else False

zbb_var_dic = { "temp_shell_para" : '',
                "temp_get" : '',
                "temp_calc" : 0 ,
                "temp_arr" : [] ,
                "temp_ret": None,
                "temp_para": Stack(),
                "temp_all": Stack()
                }

zbb_mark_dic = {}

zbb_func_dic = {}

code_text_to_list = []

line_num = 0

"""
初始化了临时存储器
- 临时存储器 tsp 用于在shell中传递参数
- 临时存储器 tc 用于储存计算参数
- 临时存储器 tp 用于储存函数参数
- 临时存储器 tr 用于储存函数返回值
- 临时存储器 ta 是通用寄存器
"""