import os
import time
from public_var import zbb_var_dic , zbb_mark_dic, code_text_to_list , line_num , isJUMP


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


def do_call(func_name:str):
    # 调用函数
    pass


def do_func(func_name:str):
    # 定义函数
    pass


def do_jump(label:str):
    # 无条件跳转
    return zbb_mark_dic[label]

def do_je(label:str,var_name1:str,var_name2:str):
    # 等于跳转
    var_name1 = int(var_name1) if var_name1.isdigit() else int(zbb_var_dic[var_name1])
    var_name2 = int(var_name2) if var_name2.isdigit() else int(zbb_var_dic[var_name2])
    isJUMP = True if var_name1 == var_name2 else None


def do_jl(label:str,var_name1:str,var_name2:str):
    # 小于跳转
    var_name1 = int(var_name1) if var_name1.isdigit() else int(zbb_var_dic[var_name1])
    var_name2 = int(var_name2) if var_name2.isdigit() else int(zbb_var_dic[var_name2])
    isJUMP = True if var_name1 <= var_name2 else None


def do_jg(label:str,var_name1:str,var_name2:str):
    # 大于跳转
    var_name1 = int(var_name1) if var_name1.isdigit() else int(zbb_var_dic[var_name1])
    var_name2 = int(var_name2) if var_name2.isdigit() else int(zbb_var_dic[var_name2])
    isJUMP = True if var_name1 >= var_name2 else None


def do_jne(label:str,var_name1:str,var_name2:str):
    # 不等于跳转
    var_name1 = int(var_name1) if var_name1.isdigit() else int(zbb_var_dic[var_name1])
    var_name2 = int(var_name2) if var_name2.isdigit() else int(zbb_var_dic[var_name2])
    isJUMP = True if var_name1 != var_name2 else None


def do_exit(x):
    exit()


def do_nop(x):
    # 无作用
    pass


def do_clean(stack_name:str):
    # 清空栈
    zbb_var_dic[stack_name].clear()


def do_push(stack_name:str, *stack_content):
    # 推至栈顶
    for item in stack_content:
        zbb_var_dic[stack_name].push(item)


def do_pop(stack_name:str):
    # 取栈顶值
    on_top_stack = zbb_var_dic[stack_name].pop()

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
    "NOP": do_nop,
    "::": do_nop
}

'''
主要部分如下
'''

def run_a_line_of_zbb( a_line_of_zbb:str ):
    this_keyword = ''
    for keyword in zbb_keywords:
        if keyword in a_line_of_zbb:
            this_keyword = keyword
            break
    else:
        raise RuntimeError(f"Grammar error when parsing\n")

    this_para = a_line_of_zbb.replace(this_keyword, '').replace(" ",'').split(",")

    func = zbb_keywords[keyword]
    for_ret = func(*this_para)

    return for_ret
