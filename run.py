from core import *

if __name__ == "__main__":
    while True:
        os.system('cls')
        if len(sys.argv) > 1: # 读取系统文件输入
            zbb_file_to_run = sys.argv[1]
            main(zbb_file_to_run)
            input_to_exit = input(f"{Fore.GREEN}Type ENTER to continue{Fore.RESET}")
            if input_to_exit == "":
                continue
            else:
                break

        print("==欢迎使用ZBB解析器==\n"
              "------------------\n"
              "请输入指令\n"
              "help 帮助\n"
              "run <文件名> 运行文件\n"
              "out 退出"
             )
        user_input = input(">>>")
        if user_input == "help":
            with open("documents/zbb_help.md", 'r', encoding='utf-8') as f:
                print(f.read())
                input_to_exit = input(f"{Fore.GREEN}Type ENTER to continue{Fore.RESET}")
                if input_to_exit == "":
                    continue
                else:
                    break

        elif user_input == "out":
            break

        elif user_input.startswith("run"):
            zbb_file_to_run = user_input.replace(" ", "").replace("run", "",1)
            try:
                main(zbb_file_to_run)
            except RuntimeError as e:
                print(f"{e}")
            except FileNotFoundError:
                print(f"{Fore.RED}File '{zbb_file_to_run}' not found{Fore.RESET}")
            input_to_exit = input(f"{Fore.GREEN}Type ENTER to continue{Fore.RESET}")
            if input_to_exit == "":
                continue
            else:
                break
        else:
            print(f"{Fore.RED}Not have introduction named {user_input}{Fore.RESET}")
            input_to_exit = input(f"{Fore.GREEN}Type ENTER to continue{Fore.RESET}")
            if input_to_exit == "":
                continue
            else:
                break