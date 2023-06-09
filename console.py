import subprocess

xterm_options = [
    '-bg', 'black',
    '-fg', 'white',
]

script_path = 'function.py'
subprocess.Popen(['xterm', '-hold', '-e', 'bash', '-c', f'/usr/bin/python3 "{script_path}"'] + xterm_options)