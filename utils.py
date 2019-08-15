class Colors:
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    clear = '\x1b[2J\x1b[H'


def print_header(text):
    print(f'{Colors.green}+{"-" * 67}+{Colors.endc}')
    print(f'{Colors.green}| {text:<64} |{Colors.endc}')
    print(f'{Colors.green}+{"-" * 67}+{Colors.endc}')


def print_line(text, value):
    print(f'{Colors.blue}{text:<14}:{Colors.endc} {Colors.bold}{Colors.red}{value:>10}{Colors.endc}')
