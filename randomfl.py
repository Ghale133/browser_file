import os
import string
import random
def random_text_file():
    current_path=os.getcwd()
    filename=input("enter the filename:")
    length=int(input("enter the length of random text:"))
    try:
        with open(os.path.join(current_path,filename),'w') as f:
            f.write(''.join(random.choices(string.ascii_lowercase+string.digits, k=length)))
            print("file is created")
    except FileNotFoundError:
        print("Directory not found")


random_text_file()