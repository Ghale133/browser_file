import os
import shutil
import random
import string

class File_handling:
    '''
    This module defines a FileBrowser class that provides functionalities 
    to perform file operations. 
    Attributes:
    current_path (str): the current path where the FileBrowser object is located.
    show_hidden (bool): a boolean flag to determine whether to show hidden files/folders or not.
    Methods:
        list_contents: displays a list of files and folders in the directory.
        rename_folder: renames a folder in the given directory.
        rename_file: renames a file in the  directory.
        create_empty_file: creates an empty file in the given directory.
        copy_file: copies a file from the given directory to a specified folder.
        copy_folder: copies a folder from the given directory to a specified folder.
        move_file: moves a file from the given directory to a specified folder.
        move_folder: moves a folder from the given directory to a specified folder.
        delete_file: deletes a file from the given directory.
        delete_folder: deletes a folder from the given directory.
        create_random_text_file: creates a file with random text in the given directory.
        view_file: displays the content of a file in the given directory.
        hide_folder: hides a folder in the current directory.
    Example:
    object= FileBrowser()
    object.list_contents()
    '''
    def list_directory(self):
        '''
        list the contents of the given directory
        os.listdir() method in python is used to get the list of all files and directories in the specified directory.
        '''
        directory_path=input("enter the directory path:")
        contents=os.listdir(directory_path)
        for item in contents:
            print(item)
            
    def rename_directory(self):
        '''
        rename the directory name  using os.rename() method.
        the method prompts to user to enter the old folder name and new folder name to be renamed
        then os.rename()method rename the folder name as the user desire.
        '''
        current_path=input("enter the current path:")
        os.rename( current_path+self.oldfolder,current_path+self.newfolder)
    
    def rename_file(self):
        '''
        rename the file name  using os.rename() method.
        the method prompts to user to enter the old file name and new new name to be renamed
        then os.rename()method rename the folder name as the user desire.
        '''
        current_path=input("enter the current_path")
        os.rename(current_path+self.oldname,current_path+self.newname)


    def copy_files(self):
        '''
        copy the file from the given directory to a specified folder.
        the method prompts to user to enter the source file name and destination location to be copied
        then shutil.copyfile()method copy the file or folder to the specified location.
        '''
        shutil.copyfile(self.source,self.destination)

    
    def copy_folder(self):
        '''
        copy the folder from the given directory to a specified location.
        the method prompts to user to enter the source folder name and destination location to be copied
        then shutil.copytree()method copy the folder to the specified location.
        '''
        shutil.copytree(self.source,self.destination)

    def empty_file(self):
        '''
        creates an empty file with the given name in the current directory.
        '''
        filename = input("enter the filename")
        current_path = os.getcwd()
        with open(os.path.join(current_path,filename), 'w') as f:
            pass
        print("file is created")

    def random_text_file(self):
        '''
         Create a new file with random text of a specified length in the current directory.
        Prompts the user to enter the name of the file to be created and the desired length of the text.
        The method then generates a string of random lowercase letters and digits using the random.choices() method
        and writes it to the new file using the with statement and the "w" flag for writing.
        If the file cannot be created due to a FileNotFoundError, an error message is printed.
        '''
        current_path=os.getcwd()
        filename=input("enter the filename:")
        length=int(input("enter the length of random text:"))
        try:
            with open(os.path.join(current_path,filename),'w') as f:
                f.write(''.join(random.choices(string.ascii_lowercase+string.digits, k=length)))
                print("file is created")
        except FileNotFoundError:
            print("Directory not found")


    def view_file(self):
        '''
        displays the content of the given file in the current directory
        '''
        with open("food.txt","r") as f:
            content=f.read()
            print(content)

    def move_folder(self):
        '''
        move the folder from the source directory to a specified location.
        the method prompts to user to enter the source folder name and destination location to be moved
        then shutil.move()method move the folder to the specified location.
        '''
        shutil.move(self.source, self.destination)

    def move_file(self):
        '''
        move the file from the source directory to a specified location.
        the method prompts to user to enter the source file name and destination location to be moved
        then os.rename()method move the file to the specified location.
        '''
        os.rename(self.source,self.destination)
 
    def delete_file(self):
        '''
        delete the file from the current location.
        prompts to user to enter the file name that is to be deleted and 
        then os.remove()method delete the file.
        '''
        file=input("enter the file to delete:")
        os.remove(file)
    
    def delete_folder(self):
        '''
        delete the folder from the current location.
        prompts to user to enter the folder name that is to be deleted and 
        then os.rmdir()method delete the given folder.
        '''
        foldername=input("enter the path")
        os.rmdir(foldername)
    
    def hide_folder(self):
        '''
        hide the folder from the current location by renaming it with putting '.'at infront of folder name.
        prompts to user to enter the folder name and its location to be hide and then
        os.rename() method hides the folder.
        '''
        
        pathfolder=os.path.join(self.path,self.foldername)
        os.rename(pathfolder,os.path.join(self.path,"."+self.foldername))
    

