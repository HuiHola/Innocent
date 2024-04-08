class banner:
    def __init__(self):
        self.BLUE="\033[94m"
        self.RED="\033[91m"
        self.GREEN="\033[92m"
        self.DONE="\033[0m"
    def show(self):
        print(f"""
        {self.BLUE}_________________
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
""")



