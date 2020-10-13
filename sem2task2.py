def nine_lines():
    three_lines()
    three_lines()
    three_lines()


def three_lines():
    new_line()
    new_line()
    new_line()

def clear_screen():
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()
    new_line()


def new_line():
    print('*')

clear_screen()

