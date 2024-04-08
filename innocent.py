import os
import subprocess
import argparse
from module import banner
from module import manu
from module import apkbuilder
import json
def poster():
    banner.banner().show()

def folderManu():
    folder_manu=manu.manu()
    manu_item=[]
    f=open("folderPath.json")
    data=json.load(f)
    for key in data:
        manu_item.append(key)
    f.close()
    manu_item.append("Custom path")
    manu_item.append("back")
    folder_manu.setManu(manu_item,"Folder Manu","select","which folder do you want to delete")
    folder_manu.showManu()
    if(folder_manu.getUserinput()=="Custom path"):
        color=manu.manu()
        print(f"{color.YELLOW}Example : DCIM/Camera{color.NONE} \n{color.BLUE}type 'back' for folder manu")
        custom_path=input(f"{color.BLUE}Costum path # {color.GREEN}")
        if(custom_path=="back"):
            folderManu()
        else:
            apkbuilder.builder().build(f"deleteFolder:{custom_path}")
    elif(folder_manu.getUserinput()=="back"):
        mainManu()
    else:
        try:
            command_file=open("folderPath.json")
            command=json.load(command_file)
            apkbuilder.builder().build(command.get(folder_manu.getUserinput()))
        except Exception as e:
            print(e)

def mainManu():
    main_manu=manu.manu()
    main_manu.setManu(["Delete File","Delete Many Files","Folder Manu"],"Main Manu","select",None)
    main_manu.showManu()
    color=manu.manu()
    if(main_manu.getUserinput()=="Delete File"):
        print(f"{color.YELLOW}Example : DCIM/Camera/myfile.jpg{color.NONE} \n{color.BLUE}type 'back' for main manu")
        deleteFilePath=input(f"{color.BLUE}Delete file path # {color.GREEN}")
        if(deleteFilePath=="back"):
            mainManu()
        else:
            apkbuilder.builder().build(f"delete:{deleteFilePath}")
    elif(main_manu.getUserinput()=="Delete Many Files"):
        print(f"{color.YELLOW}Example : DCIM/Camera/myfile.jpg,Pictures/Screenshots/ss.jpg \n{color.BLUE}type 'back' for main manu")
        deleteFilePath=input(f"{color.BLUE}Delete files path # {color.GREEN}")
        if(deleteFilePath=="back"):
            mainManu()
        else:
            apkbuilder.builder().build(f"many:{deleteFilePath}")
    elif(main_manu.getUserinput()=="Folder Manu"):
        folderManu()

def start():
    poster()
    mainManu()



start()
