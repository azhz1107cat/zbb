from core import *

if __name__ == "__main__":
    while True:
        os.system('echo ""')
        if len(sys.argv) > 1:
            zbb_file_to_run = sys.argv[1]
            main(zbb_file_to_run)

        user_input = input("***欢迎使用ZBB解析器***\n请输入指令\nhelp- 帮助\nrun- 运行文件名\nout- 退出\n>>>")
        if user_input == "help":
            with open("documents/zbb_help.md", 'r', encoding='utf-8') as f:
                print(f.read())

        elif user_input == "out":
            exit()

        elif user_input.startswith("run"):
            zbb_file_to_run = user_input.replace(" ", "").replace("run", "")
            try:
                main(zbb_file_to_run)
            except RuntimeError as e:
                print(f"\033[31m{e}\033[0m")
            except FileNotFoundError as e:
                print(f"\033[31m{e}\033[0m")

        else:
            print("\033[31mPlease input help , run or out ; window will close in 6s\033[0m")
            time.sleep(6)
