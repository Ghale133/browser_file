from browser import *
def main():
    obj=File_handling()
    while True:
        print("Available options:")
        print("1. List directory contents:")
        print("2. Rename directory:")
        print("3. Rename file:")
        print("4. Copy file:")
        print("5. copy folder:")
        print("6. create a empty file:")
        print("7. create a file from Random text file:")
        print("8. view file")
        print("9. move folder")
        print("10. Move file")
        print("11. Delete file:")
        print("12. Delete folder:")
        print("13. hide folder:")
        print("q . Quit")


        choice=input("Enter your choice: ")
        if choice=="1":
            obj.list_directory()
        elif choice=="2":
            obj.oldfolder = input("enter the old folder name:")
            obj.newfolder = input("enter the newfolder name:")
            obj.rename_directory()
        elif choice=="3":
            obj.oldname = input("enter the old file name:")
            obj.newname = input("enter the new file name:")
            obj.rename_file()
        elif choice=="4":
            obj.source=input("enter the source location with name:")
            obj.destination=input("enter the destination location with name:")
            obj.copy_files()
        elif choice=="5":
            obj.source=input("enter the source location with name:")
            obj.destination=input("enter the destination location with name:")
            obj.copy_folder()
        elif choice=="6":
            obj.empty_file()
        elif choice=="7":
            obj.random_text_file()
        elif choice=="8":
            obj.view_file()
        elif choice=="9":
            obj.source=input("enter the souce folder:")
            obj.destination=input("enter the destination folder:")
            obj.move_folder()
        elif choice=="10":
            obj.source=input("enter the filename to move:")
            obj.destination=input("enter the destination location to move:")
            obj.move_file()
        elif choice=="11":
            obj.delete_file()
        elif choice=="12":
            obj.delete_folder()
        elif choice=="13":
            obj.path=input("enter the folder path")
            obj.foldername=input("enter the folder name:")
            obj.hide_folder()
            
        elif choice=="q":
            break
            
main()
# obj.list_directory()
# obj.rename_directory()


