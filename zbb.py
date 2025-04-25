from do_zbb_ins import *
from public_var import zbb_func_dic

if __name__ == "__main__":
    with open('test/test.zbb', 'r', encoding='utf-8') as f:
        code_text = f.read()
        os.system('chcp 65001')
        print("==running==\n")
        start_time = time.time()
        code_text_to_list = code_text.split('\n')
        # 标签寻找
        func_not_end = ""
        for each_line in code_text_to_list:
            if each_line.startswith("::"):
                label = each_line.replace("::", "").replace(" ", "")
                zbb_mark_dic[label] = line_num

            if each_line.startswith("func") or each_line.startswith("FUNC"):
                func_keyword = "func" if each_line.startswith("func") else "FUNC"
                func_name =  each_line.replace(func_keyword, '').replace(" ", '')
                func_not_end = func_name
                zbb_func_dic[func_name] = {"start":line_num,
                                           "end": None,
                                           "call_from":None
                                           }
            if each_line.startswith("end") or each_line.startswith("END"):
                zbb_func_dic[func_not_end]["end"] = line_num
                func_not_end = ""

            line_num += 1

        line_num = 0
        # 阅读每一行zbb
        while True:
            if line_num < len(code_text_to_list):
                each_line_of_code = code_text_to_list[line_num]
            else: break

            if each_line_of_code == '' or each_line_of_code.startswith("//"):
                line_num += 1
                continue
            try:
                change_line_num = run_a_line_of_zbb(each_line_of_code)
                line_num = change_line_num if change_line_num is not None else line_num
            except (RuntimeError,TypeError,KeyError) as e:
                print(f"\033[31m{e}\nline {line_num+1}: { code_text_to_list[line_num] } \n {" " * (6+len(str(line_num+1)))+'^' * len(code_text_to_list[line_num]) }\n\033[0m")

                break

            line_num += 1

            if (line_num-1) == len(code_text_to_list):
                break

        end_time = time.time()
        print(f"\n==finished runtime:{ end_time - start_time }==")
        '''input_to_exit = input("Type ENTER to exit")
        exit() if input_to_exit == "" else None'''