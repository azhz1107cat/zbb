from core import *

if __name__ == "__main__":
    while True:
        os.system('cls')
        if len(sys.argv) > 1:
            zbb_file_to_run = sys.argv[1]
            main(zbb_file_to_run)

        user_input = input("==欢迎使用ZBB解析器==\n------------------\n请输入指令\nhelp 帮助\nrun <文件名> 运行文件\nout 退出\n>>>")
        if user_input == "help":
            with open("documents/zbb_help.md", 'r', encoding='utf-8') as f:
                print(f.read())
                input_to_exit = input(f"{Fore.GREEN}Type ENTER to continue{Fore.RESET}")
                if input_to_exit == "":
                    continue
                else:
                    exit()

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
            input_to_exit = input(f"{Fore.GREEN}Type ENTER to continue{Fore.RESET}")
            if input_to_exit == "":
                continue
            else:
                exit()