from core import *

if __name__ == "__main__":
    while True:
        os.system('cls')
        if len(sys.argv) > 1:
            zbb_file_to_run = sys.argv[1]
            main(zbb_file_to_run)

        user_input = input(textwrap.dedent(
            '''
            ==欢迎使用ZBB解析器==
            ------------------
            请输入指令
            help 帮助
            run <文件名> 运行文件
            out 退出
            >>>'''
        ))
        if user_input == "help":
            with open("documents/zbb_help.md", 'r', encoding='utf-8') as f:
                print(f.read())

        elif user_input == "out":
            exit()

        elif user_input.startswith("run"):
            zbb_file_to_run = user_input.replace(" ", "").replace("run", "",1)
            try:
                main(zbb_file_to_run)
            except RuntimeError as e:
                print(f"{e}")
            except FileNotFoundError as e:
                print(f"{Fore.RED}{e}{Fore.RESET}")
        else:
            print(f"{Fore.RED}Please input help , run or out ; window will close in 6s{Fore.RESET}")
            time.sleep(6)