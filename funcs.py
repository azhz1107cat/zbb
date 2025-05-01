import os
import public_var
from public_var import zbb_var_dic, zbb_mark_dic, code_text_to_list, zbb_func_dic

def zbb_data(zbb_var_name:str):

    if zbb_var_name in zbb_var_dic:

        if type(zbb_var_dic[zbb_var_name]) is int:
            return zbb_var_dic[zbb_var_name]

        elif type(zbb_var_dic[zbb_var_name]) is str:
            return zbb_var_dic[zbb_var_name]

        elif type(zbb_var_dic[zbb_var_name]) is list:
            return zbb_var_dic[zbb_var_name]
        else:
            raise RuntimeError("Type error")

    elif zbb_var_name.startswith("[") and zbb_var_name.endswith("]"):
        index_of_arr = 0
        if ":" in zbb_var_name:
            index_of_arr = zbb_data( zbb_var_name.replace("[","").replace("]","").split(":")[1] )
        else:
            index_of_arr = 0

        zbb_var_name = zbb_var_name.replace("[","").replace("]","").split(":")[0]
        if zbb_var_name not in zbb_var_dic:
            raise RuntimeError("Arr not found")

        if type(index_of_arr) is int and index_of_arr < len(zbb_var_dic[zbb_var_name]):
            return zbb_data(zbb_var_dic[zbb_var_name][index_of_arr])
        elif type(index_of_arr) is str:
            return zbb_data(zbb_var_dic[zbb_var_name][index_of_arr])
        elif index_of_arr >= len(zbb_var_dic[zbb_var_name]):
            raise RuntimeError("Index out of range")
        else:
            raise RuntimeError("Index of Array must be int")

    elif type(zbb_var_name) is int:
        return zbb_var_name

    elif zbb_var_name.isdigit():
        return int(zbb_var_name)

    elif zbb_var_name.startswith("`") and zbb_var_name.endswith("`"):
        return zbb_var_name.replace("`","")

    elif type(zbb_var_name) is str:
        return zbb_var_name

    elif type(zbb_var_name) is list:
        return zbb_var_name

    else:
        raise RuntimeError(f"please check {zbb_var_name}")


def do_move(data1:str,var_name:str):
    # 将数据移入变量
    if var_name.startswith("$"):
        raise RuntimeError("Const can not change its value")

    if var_name in zbb_var_dic:
        zbb_var_dic[var_name] = zbb_data(data1)

    elif var_name.startswith("[") and var_name.endswith("]"):
        key = var_name.replace("[","").replace("]","").split(":")[0]
        index = var_name.replace("[","").replace("]","").split(":")[1]
        index = zbb_data(index)
        if key in zbb_var_dic:
            if not (type(data1) is int ) and (data1.startswith("`") and data1.endswith("`")):
                data1 = zbb_data(data1)
            zbb_var_dic[key][index] = data1
        else:
            raise RuntimeError(f"{var_name} not in zbb_var_dic")
    else:
        raise RuntimeError(f"{var_name} not in zbb_var_dic")


def do_arr(*arr_list):
    for item in arr_list:
        zbb_var_dic["temp_arr"].append(item)


def do_use(system_ins_name:str):
    # 使用系统指令
    os.system(f"{system_ins_name} { zbb_var_dic['temp_shell_para'] }")

def do_set(var_name:str):
    # 为变量分配空间
    zbb_var_dic[var_name] = None


def do_del(var_name:str):
    # 删除变量空间
    del zbb_var_dic[var_name]


def do_add(first_num:str,second_num:str):
    # 加法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = first_num + second_num


def do_sub(first_num:str,second_num:str):
    # 减法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = first_num - second_num


def do_mult(first_num:str,second_num:str):
    # 乘法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = first_num * second_num


def do_div(first_num:str,second_num:str):
    # 除法运算
    first_num = zbb_data(first_num)
    second_num = zbb_data(second_num)
    zbb_var_dic['temp_calc'] = first_num / second_num


def do_opp(num1:str):
    # 取反运算
    zbb_var_dic['temp_calc'] = - zbb_data(num1)


def do_call(func_name:str):
    # 调用函数
    if func_name in zbb_func_dic:
        zbb_func_dic[func_name]["call_from"] = public_var.line_num
        return zbb_func_dic[func_name]["start"]
    else:
        raise RuntimeError("Function not found")


def do_func(func_name:str):
    # 定义函数
    if zbb_func_dic[func_name]["call_from"] is None:
        return zbb_func_dic[func_name]["end"]
    else:
        return None

def do_end(func_or_dic_name:str):
    # 函数结束标记
    if not func_or_dic_name in zbb_func_dic:
        return None
    if zbb_func_dic[func_or_dic_name]["call_from"] is None:
        return None
    else:
        return zbb_func_dic[func_or_dic_name]["call_from"]

def do_jump(label:str):
    # 无条件跳转
    if label in zbb_mark_dic:
        return zbb_mark_dic[label]
    else:
        raise RuntimeError("Mark not found")

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


def do_nop(*x):
    # 无作用
    pass


def do_clean(stack_name:str):
    # 清空栈
    zbb_var_dic[stack_name].clear()


def do_push(stack_name:str, *stack_content):
    # 推至栈顶
    for item in stack_content:
        zbb_var_dic[stack_name].push(zbb_data(item))


def do_pop(stack_name:str):
    # 取栈顶值
    on_top_stack = zbb_var_dic[stack_name].pop()
    zbb_var_dic["temp_get"] = on_top_stack