import subprocess
import signal
import sys
import time
import os
import readline
import commands
import styling


# def login(username, password):
#     with open('login_info.txt', 'r') as file:
#         for line in file:
#             stored_username, stored_password, permission, coloring = line.strip().split(',')
#             if username == stored_username and password == stored_password:
#                 return permission, coloring  # Return the permission (admin or mod) instead of True
#     return None  # Return None if login is unsuccessful

# ----- checks account file -----
def login(username, password):
    with open('login.txt', 'r') as file:
        for line in file:
            line_values = line.strip().split(',')
            if len(line_values) == 4:  # Check if the line has the expected number of values
                stored_username, stored_password, permission, coloring = line_values
                if username == stored_username and password == stored_password:
                    return permission, coloring  # Return the permission and coloring
    return None, None  # Return None for permission and coloring if login is unsuccessful


# ----- defines delay -----
def delay(seconds):
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break
# ----- disables ctrl C -----
def handle_ctrl_c(signum, frame):
    print("\nGood job now the code is broken and you need to restart the server")
    logged_in = False
    # raise SystemExit

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_ctrl_c)

# Enable command history and command logging
history_file = os.path.expanduser("command_log.txt")
if os.path.exists(history_file):
    readline.read_history_file(history_file)

def disable_up_down_arrows():
    readline.parse_and_bind('"\e[A":')
    readline.parse_and_bind('"\e[B":')

def enable_up_down_arrows():
    readline.parse_and_bind('"\e[A": history-search-backward')
    readline.parse_and_bind('"\e[B": history-search-forward')

def disable_logging():
    readline.set_history_length(0)

def enable_logging():
    readline.set_history_length(-1)

while True:
    logged_in = False  # Flag variable to control login loop

    while not logged_in:
        disable_up_down_arrows() # Disable up and down arrow keys
        disable_logging()
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        permission, coloring = login(username, password)  # Get the permission from the login function

        if permission is not None:  # Check if login is successful
            print("Login successful! permission:", permission)
            styling.color(coloring)
            delay(3)
            os.system('clear')
            logged_in = True  # Set the flag to break out of the login loop
        else:
            print("Invalid username or password.")

# ----- command loop -----
    while True:
        try:
            enable_logging()
            enable_up_down_arrows()  # Re-enable up and down arrow keys
            input_text = input(username + "@" + permission + ": ")
            readline.write_history_file(history_file)  # Save command to history

            cmd = input_text.split()

            mydict = {}
            for index, command in enumerate(cmd):
                var_name = "var_%d" % index
                mydict[var_name] = command
                # print(var_name + ": " + command)

            # Add more commands here
            if 'var_0' in mydict:
                var_0_value = mydict['var_0']
                if var_0_value == 'E' and 'var_1' not in mydict:
                    print("E is the best letter")
                elif var_0_value == "clear" and 'var_1' not in mydict:
                    os.system('clear')
                elif var_0_value == "help" and 'var_1' not in mydict:
                    print("Commands:\nE\nclear\nban\nexit")
                elif var_0_value == "ban":
                    commands.ban(mydict)
                elif var_0_value == "hello" and 'var_1' not in mydict:
                    print("hello world")
                elif var_0_value == "color" and 'var_2' not in mydict:
                    disable_up_down_arrows()
                    disable_logging()
                    commands.color(mydict)
                elif var_0_value == "exit" and 'var_1' not in mydict:
                    print("Logout successful!")
                    delay(2)
                    os.system('clear')
                    break
                else:
                    try:
                        # Send the command to the subprocess and get the output
                        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                        print(output.decode())
                    except subprocess.CalledProcessError as e:
                        print("Error:", e.output.decode())
        except KeyboardInterrupt:
            break
            # raise SystemExit

    # Clear command history after reaching the end
    # readline.clear_history()
    # readline.write_history_file(history_file)