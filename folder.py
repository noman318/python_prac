import os
folders = input('please enter folder names seperated by spaces: ').split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print('enter valid folder name, this folder does not exist :'+ folder)
        break
    except PermissionError:
        print('Access denied for this folder :'+ folder)
        break
    # print(files)
    for i in files:
        print(i)