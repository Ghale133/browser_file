import os
import shutil
import random
import string

class File_handling:
    def __init__(self):
        pass


#list directory contents
    def list_directory(self):
        directory_path=input("enter the directory path:")
        contents=os.listdir(directory_path)
        for item in contents:
            print(item)
            

    


#rename folder

    def rename_directory(self, oldfolder, newfolder):
        self.oldfolder = oldfolder
        self.newfolder = newfolder
        current_path=input("enter the current path:")
        os.rename( current_path+oldfolder,current_path+newfolder)
    



#rename file
    def rename_file(self,oldname, newname):
        self.oldname = oldname
        self.newname = newname
        current_path=input("enter the current_path")
        os.rename(current_path+oldname,current_path+newname)

    

#copy file
    def copy_files(self,source,destination):
        self.source= source
        self.destination=destination
        shutil.copyfile(source,destination)

    

#copy folder

    def copy_folder(self,source,destination):
        self.source=source
        self.destination=destination
        shutil.copytree(source,destination)

    

#create empty file
    def empty_file(self):
        filename = input("enter the filename")
        current_path = os.getcwd()
        with open(os.path.join(current_path,filename), 'w') as f:
            pass
        print("file is created")

    

#create file from random text
    def random_text_file(self):
        current_path=os.getcwd()
        filename=input("enter the filename:")
        length=int(input("enter the length of random text:"))
        try:
            with open(os.path.join(current_path,filename),'w') as f:
                f.write(''.join(random.choices(string.ascii_lowercase+string.digits, k=length)))
                print("file is created")
        except FileNotFoundError:
            print("Directory not found")


    

#view contents of a file
    def view_file(self):
        with open("food.txt","r") as f:
            content=f.read()
            print(content)

    def move_folder(self,source, destination):
        self.source=source
        self.destination=destination
        shutil.move(source, destination)


    
    def move_file(self,source_path, destination_path):
        self.source=source_path
        self.destination=destination_path
        os.rename(source_path, destination_path)
 

    

#delete file
    def delete_file(self):
        file=input("enter the file to delete:")
        os.remove(file)
    

#delete folder
    def delete_folder(self):
        fold=input("enter the path")
        os.rmdir(fold)
    

#hide a folder
    def hide_folder(self,path,foldername):
        self.path=path
        self.foldername=foldername
        pathfolder=os.path.join(path,foldername)
        os.rename(pathfolder,os.path.join(path,"."+foldername))
    

