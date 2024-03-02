import io
import os
import sys

from Tools.Logger import *
from Tools.Exception_arg_message import arg_message


replace_keys = [] #eg: replace_keys = [("instagram", "ddinstagram"), ("x", "y")...]

def get_current_directory(args: tuple=()):
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)#get if running as executable (PyInstaller) or any for end user...
    else:
        path = os.path.dirname(os.path.abspath(sys.argv[0]))#else if Running as .py script.
    
    if args:
        new_path = os.path.join(path, *args)
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
            
        return new_path
    else:
        os.makedirs(path, exist_ok=True)
        return path
    
    
def replace_key_words(my_input:str):
    if replace_keys:
        for _tuple in replace_keys:
            if  _tuple[1] not in my_input:
                my_input = my_input.replace(_tuple[0], _tuple[1])

        return my_input.strip()
    else:
        return my_input.strip()
    

def writeLine_to_file(a_string:str):
    try:   
        with io.open(get_current_directory(args=("Data", "values.txt")), encoding="utf-8", mode="a", newline="") as text_file:
            text_file.write(f"{replace_key_words(a_string)}\n")
        
        logger.info(f"{bcolors.WARNING}Manager{bcolors.ORIGINAL} - {a_string} copied.")
        
    except Exception as ex:
        logger.error(f"{bcolors.WARNING}Manager{bcolors.ORIGINAL} - {bcolors.FAIL}{arg_message(ex)}{bcolors.ORIGINAL}")
    