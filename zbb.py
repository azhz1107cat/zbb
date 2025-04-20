import time
from do_zbb_ins import *

if __name__ == "__main__":
    with open('test.zbb', 'r', encoding='utf-8') as f:

        code_text = f.read()
        os.system('chcp 65001')
        print("==running==\n")
        start_time = time.time()
        code_text_to_list = code_text.split('\n')
        line_num = 1
        # 阅读每一行zbb
        for each_line_of_code in code_text_to_list:
            if isJUMP or each_line_of_code == '' or each_line_of_code.startswith("//"):
                continue
            try:
                run_a_line_of_zbb(each_line_of_code)
            except (RuntimeError,TypeError,KeyError) as e:
                print(f"{e}\n in line {line_num}\n")
                break
            line_num += 1
        end_time = time.time()
        print(f"\n==finished runtime:{ end_time - start_time }==")
        '''input_to_exit = input("Type ENTER to exit")
        exit() if input_to_exit == "" else None'''