import os
import sys
import time

import colorama
from colorama import Fore

import public_var
from funcs import *
from public_var import zbb_var_dic, zbb_mark_dic, code_text_to_list, zbb_func_dic

'''
关键字表
'''

zbb_keywords = {
    "USE": do_use,
    "SET": do_set,
    "DEL": do_del,
    "FUNC": do_func,
    "END": do_end,
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
    "ARR": do_arr,
    "DIC": do_nop,
    "ITEM": do_nop,
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

def run_a_line_of_zbb( a_line_of_zbb:str):
    this_keyword = ''
    for keyword in zbb_keywords:
        if a_line_of_zbb.replace(" ",'').startswith(keyword):
            this_keyword = keyword
            this_para = a_line_of_zbb.replace(" ", '').replace(this_keyword, '',1).split(",")
            break

        if  a_line_of_zbb.replace(" ",'').startswith(keyword.lower()):
            this_keyword = keyword
            this_para = a_line_of_zbb.replace(" ", '').replace(this_keyword.lower(), '',1).split(",")
            break
    else:
        raise RuntimeError(f"Grammar error when parsing\n")


    zbb_do = zbb_keywords[ this_keyword ]
    for_ret = zbb_do(*this_para)

    return for_ret


def main(zbb_file_to_run):
    """
    打开文件并解析
    """

    with open(zbb_file_to_run, 'r', encoding='utf-8') as f:
        public_var.line_num = 0
        code_text = f.read()
        os.system('chcp 65001')
        print("==running==\n")
        start_time = time.time()
        code_text_to_list = code_text.split('\n')

        """
        标签、函数、字典预定义
        """
        temp_dic_ = {}
        dic_not_end = ""
        func_not_end = ""
        for each_line in code_text_to_list:
            if each_line.replace(" ","").startswith("::"):
                label = each_line.replace("::", "",1).replace(" ", "")
                zbb_mark_dic[label] = public_var.line_num

            if each_line.startswith("func") or each_line.startswith("FUNC"):
                func_keyword = "func" if each_line.startswith("func") else "FUNC"
                func_name = each_line.replace(func_keyword, '',1).replace(" ", '')
                func_not_end = func_name
                zbb_func_dic[func_name] = {"start": public_var.line_num,
                                           "end": None,
                                           "call_from": None
                                           }
            if each_line.replace(" ","").startswith("dic") or each_line.startswith("DIC"):
                dic_keyword = "dic" if each_line.startswith("dic") else "DIC"
                dic_name = each_line.replace(dic_keyword, '',1).replace(" ", '')
                dic_not_end = dic_name

            if each_line.replace(" ","").startswith("end") or each_line.startswith("END"):
                if dic_not_end != "":
                    zbb_var_dic[dic_not_end] = temp_dic_
                    temp_dic_ = {}
                    dic_not_end = ""

                elif dic_not_end == "":
                    zbb_func_dic[func_not_end]["end"] = public_var.line_num
                    func_not_end = ""

            if each_line.replace(" ","").startswith("item") or each_line.startswith("ITEM"):
                item_keyword = "item" if each_line.replace(" ","").startswith("item") else "ITEM"
                item_key = each_line.replace(item_keyword, '',1).replace(" ", '').split(",")[0]
                item_value = each_line.replace(item_keyword, '', 1).replace(" ", '').split(",")[1]
                temp_dic_[zbb_data(item_key)] = zbb_data(item_value)

            public_var.line_num += 1

        if dic_not_end != "" :
            print(f"{Fore.RED}Dic not end:",Fore.RESET)
        if func_not_end != "" :
            print(f"{Fore.RED}Func not end", Fore.RESET)

        public_var.line_num = 0

        """
        阅读每一行zbb
        """
        while True:
            if public_var.line_num < len(code_text_to_list):
                each_line_of_code = code_text_to_list[public_var.line_num]
            else:
                break

            if each_line_of_code == '' or each_line_of_code.startswith("//"):
                public_var.line_num += 1
                continue
            try:
                change_line_num = run_a_line_of_zbb(each_line_of_code)
                public_var.line_num = change_line_num if change_line_num is not None else public_var.line_num
            except (RuntimeError, TypeError, KeyError) as e:
                print(
                    f"{Fore.RED}{e}\nline {public_var.line_num + 1}: {code_text_to_list[public_var.line_num]} \n {" " * (6 + len(str(public_var.line_num + 1))) + '^' * len(code_text_to_list[public_var.line_num])}\n{Fore.RESET}"
                )
                break

            except Exception as e:
                print(f"{Fore.RED}UnSupport error:", e , Fore.RESET)

            public_var.line_num += 1

            if public_var.line_num - 1 == len(code_text_to_list):
                break

        end_time = time.time()
        print(f"\n==program done\nruntime:{end_time - start_time}==")