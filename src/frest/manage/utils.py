import os
from .bcolors import COLORS 


ENDC = len(COLORS) - 1

def logging(text, _type=ENDC, end=""):
    print(f"{COLORS[_type]}{text}{COLORS[ENDC]}", end=end)


def logging_arg(text, *args):
    args = [f"{COLORS[0]}{i}{COLORS[ENDC]}" for i in args]
    print(text.format(*args), end="")

def logo():
    print(
        """  
   __               _    
  / _|             | |   
 | |_ _ __ ___  ___| |_ 
 |  _| '__/ _ \/ __| __| 
 | | | | |  __/\__ \ |_  
 |_| |_|  \___||___/\__|
    \n\n"""
    )


def create_app(name):
    pass
