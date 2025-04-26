from do_zbb_ins import *

def main(zbb_file_to_run):
    # 打开文件并解析
    with open(zbb_file_to_run, 'r', encoding='utf-8') as f:
        public_var.line_num = 0
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
                zbb_mark_dic[label] = public_var.line_num

            if each_line.startswith("func") or each_line.startswith("FUNC"):
                func_keyword = "func" if each_line.startswith("func") else "FUNC"
                func_name = each_line.replace(func_keyword, '').replace(" ", '')
                func_not_end = func_name
                zbb_func_dic[func_name] = {"start": public_var.line_num,
                                           "end": None,
                                           "call_from": None
                                           }
            if each_line.startswith("end") or each_line.startswith("END"):
                zbb_func_dic[func_not_end]["end"] = public_var.line_num
                func_not_end = ""

            public_var.line_num += 1

        public_var.line_num = 0
        # 阅读每一行zbb
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
                    f"\033[31m{e}\nline {public_var.line_num + 1}: {code_text_to_list[public_var.line_num]} \n {" " * (6 + len(str(public_var.line_num + 1))) + '^' * len(code_text_to_list[public_var.line_num])}\n\033[0m")
                break
            public_var.line_num += 1

            if (public_var.line_num - 1) == len(code_text_to_list):
                break

        end_time = time.time()
        print(f"\n==done runtime:{end_time - start_time}==")
        input_to_exit = input("Type ENTER to continue")
        if input_to_exit == "":
            return
        else:
            exit()

if __name__ == "__main__":
    while True:
        if len(sys.argv) > 1:
            zbb_file_to_run = sys.argv[1]
            main(zbb_file_to_run)

        user_input = input("***欢迎使用ZBB解析器***\n请输入指令\nhelp- 帮助\nrun- 运行文件名\nout- 退出\n>>>")
        if user_input == "help":
            with open("documents/zbb_help.md", 'r', encoding='utf-8') as f:
                print(f.read())

        elif user_input == "out":
            break

        elif user_input.startswith("run"):
            zbb_file_to_run = user_input.replace(" ", "").replace("run", "")
            main(zbb_file_to_run)

        else:
            print("\033[31mPlease input help , run or out\033[0m")
