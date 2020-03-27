class bcolors(object):
    DARK_GREY = "\033[90m"
    BOLD = "\033[1m"
    ERROR = "\033[91m"
    OK = "\033[92m"
    WARNING = "\033[93m"
    ENDC = "\033[0m"


COLORS = [
    bcolors.DARK_GREY,
    bcolors.BOLD,
    bcolors.ERROR,
    bcolors.OK,
    bcolors.WARNING,
    bcolors.ENDC,
]
ENDC = len(COLORS) - 1


def logging(text, _type=ENDC, end=""):
    print(f"{COLORS[_type]}{text}{COLORS[ENDC]}", end=end)


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
