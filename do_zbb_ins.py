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
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = str(first_num + second_num)


def do_sub(first_num:str,second_num:str):
    # 减法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = str(first_num - second_num)


def do_mult(first_num:str,second_num:str):
    # 乘法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = str(first_num * second_num)


def do_div(first_num:str,second_num:str):
    # 除法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = str(first_num / second_num)


def do_opp(num1:str):
    # 取反运算
    zbb_var_dic['temp_calc'] = - zbb_data(num1)


def do_move(data1:str,var_name:str):
    # 将数据移入变量
    zbb_var_dic[var_name] = zbb_data(data1)


def do_call(func_name:str):
    # 调用函数
    pass


def do_func(func_name:str):
    # 定义函数
    pass


def do_jump(label:str):
    # 无条件跳转
    return zbb_mark_dic[label]

def do_je(label:str,var_name1:str,var_name2:str,else_label:str):
    # 等于跳转
    if zbb_data(var_name1) == zbb_data(var_name2):
        return zbb_mark_dic[label]
    else:
        return zbb_mark_dic[else_label]


def do_jl(label:str,var_name1:str,var_name2:str,else_label:str):
    # 小于跳转
    try:
        if zbb_data(var_name1) < zbb_data(var_name2):
            return zbb_mark_dic[label]
        else:
            return zbb_mark_dic[else_label]
    except KeyError as e:
        raise RuntimeError(f"{e} : Mark not found")
    except TypeError as e:
        raise RuntimeError(f"{e} : Compare error")


def do_jg(label:str,var_name1:str,var_name2:str,else_label:str):
    # 大于跳转
    try:
        if zbb_data(var_name1) > zbb_data(var_name2):
            return zbb_mark_dic[label]
        else:
            return zbb_mark_dic[else_label]
    except KeyError as e:
        raise RuntimeError(f"{e} : Mark not found")
    except TypeError as e:
        raise RuntimeError(f"{e} : Compare error")


def do_jne(label:str,var_name1:str,var_name2:str,else_label:str):
    # 不等于跳转
    try:
        if zbb_data(var_name1) != zbb_data(var_name2):
            return zbb_mark_dic[label]
        else:
            return zbb_mark_dic[else_label]
    except KeyError as e:
        raise RuntimeError(f"{e} : Mark not found")
    except TypeError as e:
        raise RuntimeError(f"{e} : Compare error")


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
    zbb_var_dic["temp_get_ret"] = on_top_stack

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
def zbb_data(zbb_var_name:str):
    if zbb_var_name in zbb_var_dic:
        return zbb_var_dic[zbb_var_name]
    elif zbb_var_name.isdigit():
        return int(zbb_var_name)
    elif zbb_var_name.startswith("`") and zbb_var_name.endswith("`"):
        return zbb_var_name.replace("`","")
    else:
        raise RuntimeError(f"{zbb_var_name} not in zbb_var_dic")


def run_a_line_of_zbb( a_line_of_zbb:str ):
    this_keyword = ''
    for keyword in zbb_keywords:
        if keyword in a_line_of_zbb:
            this_keyword = keyword
            this_para = a_line_of_zbb.replace(this_keyword, '').replace(" ", '').split(",")
            break

        if  keyword.lower() in a_line_of_zbb:
            this_keyword = keyword
            this_para = a_line_of_zbb.replace(this_keyword.lower(), '').replace(" ", '').split(",")
            break
    else:
        raise RuntimeError(f"Grammar error when parsing\n")



    zbb_do = zbb_keywords[ this_keyword ]
    for_ret = zbb_do(*this_para)

    return for_ret