class banner:
    def __init__(self):
        self.BLUE="\033[94m"
        self.RED="\033[91m"
        self.GREEN="\033[92m"
        self.YELLOW="\033[93m"
        self.DONE="\033[0m"
    def show(self):
        print(f"""
        {self.BLUE}_________________
        |   . ====      |
        |               |
        |    {self.RED}PROOF{self.BLUE}      |
        |    {self.RED}Deleted{self.BLUE}    |
        |               |
        |               |
        |               |
        |               |
        |               |
        |               |
        |_______________|
        |   {self.BLUE}HUI HOLA    |
        |_______________|

           {self.GREEN}I am {self.RED}INNOCENT{self.DONE}

    {self.RED}-------------------------------------------
    |{self.BLUE}  auther : {self.GREEN}HUI HOLA                   {self.RED}   |
   {self.RED} |                                         |
   {self.RED} |{self.BLUE}  Github : {self.GREEN}https://github.com/HuiHola{self.DONE}{self.RED}    |
    {self.RED}-------------------------------------------""")


