from colorama import init, Fore, Back, Style
import os
import subprocess

file_path = 'login_info.txt'

def color(coloring):
    if coloring == "0":
        change_xterm_colors("000000", "FFFFFF")
        write_color("0")
    elif coloring == "1":
        change_xterm_colors("FFFFFF", "000000")
        write_color("1")
    elif coloring == "2":
        change_xterm_colors("000000", "0000FF")
        write_color("2")
    elif coloring == "3":
        change_xterm_colors("000000", "00FF00")
        write_color("3")
        
def change_xterm_colors(background_color, text_color):
    # Generate the ANSI escape sequence for background color
    background_seq = f'\033]11;#{background_color}\007'
    text_seq = f'\033]10;#{text_color}\007'

    subprocess.run(['echo', '-ne', background_seq])
    subprocess.run(['echo', '-ne', text_seq])

# ----- edit the coloring in the user file
def write_color(color):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_index = 0
    line_parts = lines[line_index].strip().split(',')
    line_parts[-1] = color

    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i == line_index:
                file.write(','.join(line_parts) + '\n')
            else:
                file.write(line)
