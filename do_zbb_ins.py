import os
from public_var import *

def do_use(system_ins_name:str):
    # 使用系统指令
    os.system(f"{system_ins_name} { zbb_var_dic['temp_shell_para'] }")
    zbb_var_dic['temp_shell_para'] = ''

def do_set(var_name:str):
    # 为变量分配空间
    zbb_var_dic[var_name] = ''


def do_del(var_name:str):
    # 删除变量空间
    del zbb_var_dic[var_name]


def do_add(first_num:str,second_num:str):
    # 加法运算
    first_num = int(first_num) if first_num.isdigit() else int(zbb_var_dic[first_num])
    second_num = int(second_num) if second_num.isdigit() else int(zbb_var_dic[second_num])
    zbb_var_dic['temp_calc'] = str(first_num + second_num)


def do_sub(first_num:str,second_num:str):
    # 减法运算
    first_num = int(first_num) if first_num.isdigit() else int(zbb_var_dic[first_num])
    second_num = int(second_num) if second_num.isdigit() else int(zbb_var_dic[second_num])
    zbb_var_dic['temp_calc'] = str(first_num - second_num)


def do_mult(first_num:str,second_num:str):
    # 乘法运算
    first_num = int(first_num) if first_num.isdigit() else int(zbb_var_dic[first_num])
    second_num = int(second_num) if second_num.isdigit() else int(zbb_var_dic[second_num])
    zbb_var_dic['temp_calc'] = str(first_num * second_num)


def do_div(first_num:str,second_num:str):
    # 除法运算
    first_num = int(first_num) if first_num.isdigit() else int(zbb_var_dic[first_num])
    second_num = int(second_num) if second_num.isdigit() else int(zbb_var_dic[second_num])
    zbb_var_dic['temp_calc'] = str(first_num / second_num)


def do_opp(num1:str):
    # 取反运算
    zbb_var_dic['temp_calc'] = -int(num1) if num1.isdigit() else -int(zbb_var_dic[num1])


def do_move(data1:str,var_name:str):
    # 将数据移入变量
    if data1.isdigit() :
        zbb_var_dic[var_name] = data1

    elif data1.startswith("`") and data1.endswith("`"):
        zbb_var_dic[var_name] = data1.replace("`",'')

    else:
        zbb_var_dic[var_name] = zbb_var_dic[data1]

def do_func(func_name:str):
    # 定义函数
    pass


def do_jump(line_num:int):
    # 无条件跳转
    isJUMP = True

def do_je(line_num:int,var_name1:str,var_name2:str):
    # 等于跳转
    pass


def do_jl(line_num:int,var_name1:str,var_name2:str):
    # 小于跳转
    pass


def do_jg(line_num:int,var_name1:str,var_name2:str):
    # 大于跳转
    pass


def do_jne(line_num:int,var_name1:str,var_name2:str):
    # 不等于跳转
    pass


def do_exit():
    exit()


def do_call(func_name:str):
    # 调用函数
    pass


def do_clean(stack_name:str):
    # 清空栈
    pass


def do_push(stack_name:str):
    # 推至栈顶
    pass


def do_pop(stack_name:str):
    # 取栈顶值
    pass


def do_nop():
    # 无作用
    pass

'''
关键字表
'''

zbb_keywords = {
    "USE": do_use,
    "SET": do_set,
    "DEL": do_del,
    "FUNC": do_func,
    "ADD": do_add,
    "SUB": do_sub,
    "MULT": do_mult,
    "DIV": do_div,
    "OPP": do_opp,
    "MOVE": do_move,
    "JUMP": do_jump,
    "JE": do_je,
    "JL": do_jl,
    "JG": do_jg,
    "JNE": do_jne,
    "EXIT": do_exit,
    "CALL": do_call,
    "CLEAN": do_clean,
    "PUSH": do_push,
    "POP": do_pop,
    "NOP": do_nop
}

'''
主要部分如下
'''

def zbb_do(keyword:str , para:list ):
    func = zbb_keywords[keyword]
    func(*para)

def run_a_line_of_zbb( a_line_of_zbb:str ):
    this_keyword = ''
    for keyword in zbb_keywords:
        if keyword in a_line_of_zbb:
            this_keyword = keyword
            break
    else:
        raise RuntimeError(f"Grammar error when parsing \n {a_line_of_zbb} \n {'^' * len(a_line_of_zbb)}")

    this_para = a_line_of_zbb.replace(this_keyword, '').replace(" ",'').split(",")
    zbb_do(this_keyword,this_para)