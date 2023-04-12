import os


def rename_directory(oldfolder, newfolder):

    dir=input("enter the path:") 
    os.rename( dir+oldfolder,dir+newfolder)
rename_directory(input("enter old folder:"),input("enter new folder:"))


# def rename_file(oldname, newname):
#     os.rename(dir+oldname,dir+newname)

# rename_file(input("enter old name: "),input("enter new name: "))
