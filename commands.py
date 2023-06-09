import styling

# ----- ban command -----
def ban(mydict):
    if 'var_1' not in mydict:
        print("ban: the user is empty")
    elif 'var_2' not in mydict:
        var_1_value = mydict['var_1']
        print("ban: " + var_1_value + " has been banned forever")
    elif 'var_3' in mydict:
        print('ban: the command runs "ban username time" and no more')
    else:
        var_1_value = mydict['var_1']
        var_2_value = mydict['var_2']
        if "d" in var_2_value:
            if "1d" in var_2_value:
                print("ban: " + var_1_value + " is banned for " + var_2_value + " day")
            else:
                print("ban: " + var_1_value + " is banned for " + var_2_value + " days")
        elif "h" in var_2_value:
            if "1h" in var_2_value:
                print("ban: " + var_1_value + " is banned for " + var_2_value + " hour")
            else:
                print("ban: " + var_1_value + " is banned for " + var_2_value + " hours")

# ----- coloring commands -----
def color(mydict):
    if 'var_1' not in mydict:
        clr = input("pick color options: ")
        styling.color(clr)
    else:
        var_1_value = mydict['var_1']
        if var_1_value == "help":
            color_help()
        elif var_1_value == "reset":
            color_reset()



def color_help():
    color_help_response ='''
0:
    - Background: black
    - Text color: white
1:
    - Background: 
    - Text color: 
2:
    - Background: 
    - Text color: 
3:
    - Background: 
    - Text color: 
    '''
    print(color_help_response)

# ----- example command with sub cmds ----
def your_function_name(mydict):
    if 'var_1' not in mydict:
        print(mydict)
    else:
        var_1_value = mydict['var_1']
        if var_1_value == "example":
            print(mydict)
        elif var_1_value == "help":
            print(mydict)
            