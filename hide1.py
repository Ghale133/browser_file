import os 
def hd_folder():
    path=input("enter the path")
    os.rename(path,"./.flowers")
hd_folder()